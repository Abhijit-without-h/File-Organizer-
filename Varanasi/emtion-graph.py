import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

class EmotionAnalyzer:
    def __init__(self):
        pass

    def load_data(self, file_path):
        """Load and preprocess the data"""
        df = pd.read_csv(file_path)
        if 'Emotion' in df.columns:
            df['Emotion'] = df['Emotion'].fillna('').str.lower()
        else:
            raise ValueError("The 'emotion' column is not found in the CSV file. Please check the file structure.")

        if 'Keywords' in df.columns:
            df['Keywords'] = df['Keywords'].fillna('').str.lower()
        else:
            raise ValueError("The 'keywords' column is not found in the CSV file. Please check the file structure.")

        return df

    def split_emotions(self, df):
        """Split comma-separated emotions into separate rows"""
        # Expand comma-separated emotions into individual rows
        df = df.drop('Emotion', axis=1).join(
            df['Emotion'].str.split(',', expand=True).stack().reset_index(level=1, drop=True).rename('Emotion')
        )
        df['Emotion'] = df['Emotion'].str.strip()  # Remove any extra whitespace
        return df

    def generate_word_cloud(self, text, title, output_path):
        """Generate and save word cloud"""
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            colormap='viridis',
            max_words=100
        ).generate(text)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(title)
        plt.savefig(output_path, bbox_inches='tight', dpi=300)
        plt.close()

    def analyze_emotions(self, df, location_name):
        """Analyze emotion and generate visualizations for a location"""
        # Split emotions into separate rows
        df = self.split_emotions(df)

        # Create a pie chart for emotions
        emotion_counts = df['Emotion'].value_counts()
        plt.figure(figsize=(8, 6))
        colors = sns.color_palette('pastel')[:len(emotion_counts)]
        plt.pie(
            emotion_counts,
            labels=emotion_counts.index,
            autopct='%1.1f%%',
            startangle=140,
            colors=colors
        )
        plt.title(f'Emotion Distribution - {location_name}')
        plt.savefig(f'{location_name}_emotion_pie_chart.png')
        plt.close()

        # Create a bar chart for emotions
        plt.figure(figsize=(10, 6))
        sns.barplot(x=emotion_counts.index, y=emotion_counts.values, palette='viridis')
        plt.title(f'Emotion Frequency - {location_name}')
        plt.xlabel('Emotion')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'{location_name}_emotion_bar_chart.png')
        plt.close()

        # Generate a word cloud for emotions
        all_emotions_text = ' '.join(df['Emotion'])
        self.generate_word_cloud(
            all_emotions_text,
            f'Word Cloud - Emotions - {location_name}',
            f'{location_name}_emotions_word_cloud.png'
        )

        print(f"Emotion analysis for {location_name} complete.")
        print(f"Pie chart saved as '{location_name}_emotion_pie_chart.png'")
        print(f"Bar chart saved as '{location_name}_emotion_bar_chart.png'")
        print(f"Word cloud saved as '{location_name}_emotions_word_cloud.png'")

# Usage example
if __name__ == "__main__":
    analyzer = EmotionAnalyzer()
    df = analyzer.load_data('/content/Telegram Web Test 2.csv')
    analyzer.analyze_emotions(df, "varanasi")

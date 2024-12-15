import matplotlib.pyplot as plt
import seaborn as sns

def plot_headline_length_distribution(df, column_name="headline_length"):
    """
    Plots the distribution of headline lengths.
    
    Parameters:
    - df (pd.DataFrame): DataFrame containing the headline_length column.
    - column_name (str): Name of the column with headline lengths.
    """
    sns.histplot(df[column_name], kde=True, bins=50)
    plt.title("Distribution of Headline Lengths")
    plt.xlabel("Headline Length")
    plt.ylabel("Frequency")
    plt.show()

def plot_publication_trends(publication_trends):
    """
    Plots publication trends over time.
    
    Parameters:
    - publication_trends (pd.Series): Publication counts per date.
    """
    plt.figure(figsize=(10, 6))
    publication_trends.plot()
    plt.title("Publication Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.grid()
    plt.show()

def plot_top_publishers(article_counts, top_n=10):
    """
    Plots the top N publishers by article count.
    
    Parameters:
    - article_counts (pd.Series): Article counts per publisher.
    - top_n (int): Number of top publishers to display.
    """
    top_publishers = article_counts.head(top_n)
    top_publishers.plot(kind='bar', figsize=(10, 6), color='skyblue')
    plt.title(f"Top {top_n} Publishers by Article Count")
    plt.xlabel("Publisher")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=45)
    plt.show()
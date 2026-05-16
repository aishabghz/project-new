# %%
!pip install streamlit matplotlib pandas


# %%


import pandas as pd
import matplotlib.pyplot as plt


# %%
df = pd.read_csv("netflix_titles.csv")

# %%
df = df.drop_duplicates()

# %%
df['director'].fillna("Inconnu", inplace=True)
df['cast'].fillna("Inconnu", inplace=True)
df['country'].fillna("Inconnu", inplace=True)
df['rating'].fillna("Non classé", inplace=True)


# %%
df = df.dropna(subset=['date_added'])

# %%
df['date_added'] = df['date_added'].str.strip()


# %%
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# %%
df['year_added'] = df['date_added'].dt.year

# %%
options=df['type'].unique()
default=df['type'].unique()

# %%
int(df['release_year'].min()),
int(df['release_year'].max()),

# %%
top_countries = df["country"].value_counts().head(10)

top_countries.plot(kind="bar")

plt.title("Top 10 des pays avec le plus de contenus Netflix")
plt.xlabel("Pays")
plt.ylabel("Nombre de contenus")

plt.xticks(rotation=60)

plt.show()

# %%
types = df["type"].value_counts()

plt.figure(facecolor="white")

plt.pie(types,
        labels=types.index,
        autopct='%1.1f%%',
        startangle=90)

plt.title("Répartition des contenus Netflix : Films vs Séries")

plt.axis("equal")

plt.show()


# %%
genres = df["listed_in"].str.split(', ').explode()

top_genres = genres.value_counts().head(10)

plt.figure(figsize=(10,6))

top_genres.sort_values().plot(kind="barh")

plt.title("Top 10 des genres les plus présents sur Netflix")
plt.xlabel("Nombre de contenus")
plt.ylabel("Genres")

plt.grid(axis="x", linestyle="--", alpha=0.7)

plt.show()

# %%
ages = df["rating"].value_counts()

mapping = {
    "G": "Enfants",
    "TV-Y": "Enfants",
    "TV-Y7": "Enfants",
    "PG": "Jeunes",
    "TV-PG": "Jeunes",
    "TV-14": "Adolescents",
    "R": "Adultes",
    "TV-MA": "Adultes"
}

ages = ages.index.to_series().map(mapping).value_counts()

plt.figure(figsize=(6,6), facecolor="white")

plt.pie(
    ages,
    labels=ages.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Répartition des tranches d'âge sur Netflix")

plt.axis("equal")

plt.show()


# %%
years = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(10,5))

years.plot(kind="line", marker="o")

plt.title("Évolution des contenus Netflix par année")
plt.xlabel("Année")
plt.ylabel("Nombre de contenus")

plt.grid(True, linestyle="--", alpha=0.5)

plt.show()
# --- Graphique 1 : Top 10 des pays ---
top_countries = df["country"].value_counts().head(10)
top_countries.plot(kind="bar")
plt.title("Top 10 des pays avec le plus de contenus Netflix")
plt.xlabel("Pays")
plt.ylabel("Nombre de contenus")
plt.xticks(rotation=45)
plt.show()

# --- Graphique 2 : Répartition Films vs Séries ---
types = df["type"].value_counts()
plt.figure(facecolor="white")
plt.pie(types,
        labels=types.index,
        autopct='%1.1f%%',
        startangle=90)
plt.title("Répartition des contenus Netflix : Films vs Séries")
plt.axis("equal")
plt.show()

# --- Graphique 3 : Top 10 des genres ---
genres = df["listed_in"].str.split(', ').explode()
top_genres = genres.value_counts().head(10)
plt.figure(figsize=(10,6))
top_genres.sort_values().plot(kind="barh")
plt.title("Top 10 des genres les plus présents sur Netflix")
plt.xlabel("Nombre de contenus")
plt.ylabel("Genres")
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.show()

# --- Graphique 4 : Répartition par tranches d'âge ---
ages = df["rating"].value_counts()
mapping = {
    "G": "Enfants",
    "TV-Y": "Enfants",
    "TV-Y7": "Enfants",
    "PG": "Jeunes",
    "TV-PG": "Jeunes",
    "TV-14": "Adolescents",
    "R": "Adultes",
    "TV-MA": "Adultes"
}
ages = ages.index.to_series().map(mapping).value_counts()
plt.figure(figsize=(6,6), facecolor="white")
plt.pie(
    ages,
    labels=ages.index,
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Répartition des tranches d'âge sur Netflix")
plt.axis("equal")
plt.show()

# %%
movies = df[df["type"] == "Movie"]

movies["duration"] = movies["duration"].str.replace(" min", "")
movies["duration"] = pd.to_numeric(movies["duration"], errors="coerce")

movies["duration"].hist(bins=20)

plt.title("Répartition des durées des films Netflix")
plt.xlabel("Durée des films (en minutes)")
plt.ylabel("Nombre de films")

plt.show()



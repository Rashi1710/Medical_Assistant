import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def age_group_to_numeric(age_group):
    if 'Child' in age_group:
        return 18
    else:
        return 18

def recommend_doctors(symptoms, age, location):
    # Load data
    symptoms_df = pd.read_csv('symptoms_data.csv')
    providers_df = pd.read_csv('provider_data.csv')

    # Filter providers by location
    providers_df = providers_df[providers_df['Location'] == location]

    # Combine symptom descriptions for each provider
    provider_symptoms = symptoms_df.groupby('Provider_ID')['Symptom'].apply(' '.join).reset_index()

    # Initialize TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform symptom descriptions
    symptom_matrix = vectorizer.fit_transform(provider_symptoms['Symptom'])

    # Transform user symptoms
    user_symptoms_str = ' '.join(symptoms)
    user_symptom_vector = vectorizer.transform([user_symptoms_str])

    # Compute cosine similarity between user symptoms and provider symptoms
    similarity_scores = cosine_similarity(user_symptom_vector, symptom_matrix)

    # Get top matching providers
    top_providers_indices = similarity_scores.argsort(axis=1)[0][-5:][::-1]  # Top 5 providers
    top_providers = provider_symptoms.iloc[top_providers_indices]['Provider_ID']

    # Filter providers by age group
    filtered_providers = providers_df.copy()
    filtered_providers['Age'] = filtered_providers['Age Group'].apply(age_group_to_numeric)
    filtered_providers = filtered_providers[(filtered_providers['Age'] >= age) | 
                                            ((filtered_providers['Age'] < age) & (filtered_providers['Age Group'].str.contains('Child')))]

    # Sort providers by ratings
    filtered_providers = filtered_providers[filtered_providers['Provider_ID'].isin(top_providers)]
    filtered_providers = filtered_providers.sort_values(by='Rating', ascending=False)

    return filtered_providers
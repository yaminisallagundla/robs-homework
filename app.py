import streamlit as st
import openai
from dotenv import load_dotenv

openai.api_key = load_dotenv('OPENAI_API_KEY')

def generate_story(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=500,
        n = 1,
        stop=None,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    story = response.choices[0].text.strip()
    return story

def main():
    st.title('Story Generator')

    # Prompt input
    prompt = st.text_input('Enter a starting sentence:')

    if st.button('Generate Story'):
        if prompt:
            story = generate_story(prompt)
            st.subheader('Generated Story')
            st.write(story)
        else:
            st.warning('Please enter a story prompt.')

if __name__ == '__main__':
    main()


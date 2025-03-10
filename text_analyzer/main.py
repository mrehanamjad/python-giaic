import streamlit as st

def count_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1

    return vowel_count

def analyze_text():
    paragraph = st.session_state.paragraph
    if paragraph.strip():  
        words = paragraph.split()
        st.session_state.word_count = len(words)
        st.session_state.char_count = len(paragraph)
        st.session_state.vowel_count = count_vowels(paragraph)
        st.session_state.modified_paragraph = paragraph
        st.session_state.contains_python = "Python" in paragraph
        st.session_state.avg_word_length = st.session_state.char_count / st.session_state.word_count

    else:
        st.warning("⚠️ Please enter a valid paragraph.")

def replace_word():
    if st.session_state.search_word and st.session_state.replace_word:
        st.session_state.modified_paragraph = st.session_state.modified_paragraph.replace(
            st.session_state.search_word, st.session_state.replace_word
        )
    else:
        st.warning("⚠️ Please enter both words to perform replacement.")

def main():
    st.set_page_config(
        page_title="Text Analyzer",
        page_icon="🧪",
        layout="centered"
    )
    st.title("🧪 Text Analyzer")
    
    if "word_count" not in st.session_state:
        st.session_state.word_count = 0
        st.session_state.char_count = 0
        st.session_state.vowel_count = 0
        st.session_state.modified_paragraph = ""
        st.session_state.contains_python = False
        st.session_state.avg_word_length = 0.0
    
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    
    if uploaded_file is not None:
        file_contents = uploaded_file.getvalue().decode("utf-8")
        st.session_state.paragraph = file_contents
    else:
        st.session_state.paragraph = st.text_area("Enter a paragraph:", "", height=200)
    
    if st.button("🔍 Analyze Text"):
        analyze_text()
    
    if st.session_state.word_count > 0:
        st.markdown("## 📊 Analysis Results")
        st.success(f"**Total Words:** {st.session_state.word_count}")  
        st.info(f"**Total Characters (including spaces):** {st.session_state.char_count}")
        st.warning(f"**Total Vowels:** {st.session_state.vowel_count}")
        
        with st.expander("🔍 Search and Replace"):
            st.session_state.search_word = st.text_input("Enter word to search:")
            st.session_state.replace_word = st.text_input("Enter replacement word:")
            if st.button("🔄 Replace Word"):
                replace_word()
            st.write("**Modified Paragraph:**")
            st.code(st.session_state.modified_paragraph, language="text")
        
        with st.expander("🔠 Text Transformations"):
            st.write("**Uppercase:**")
            st.code(st.session_state.modified_paragraph.upper(), language="text")
            st.write("**Lowercase:**")
            st.code(st.session_state.modified_paragraph.lower(), language="text")
        
        st.markdown("## 🔎 Additional Insights")
        st.success(f"**Contains 'Python'?:** {st.session_state.contains_python}")  
        st.info(f"**Average Word Length:** {st.session_state.avg_word_length:.2f}") 

if __name__ == "__main__":
    main()

mkdir -p ~/.streamlit/credentials.toml

eco "\
[server]\n\
port=$PORT\n\
enableCORS=false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
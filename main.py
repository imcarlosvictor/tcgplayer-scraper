import random
import requests
import pandas as pd
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_currency_rate() -> None:
    """
    Get live currency rate
    """

    URL = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=CAD'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    while True:
    pass


class TCGPlayerData:
    def __init__(self):
        st.set_page_config(layout='wide')
        self.tab1, self.tab2 = st.tabs(['One Piece', 'YuGiOh'])


    def create_one_piece_tab(self):
        with self.tab1:
            st.text('Last Updated: ')
            # Trending cards
            top_3 = st.container(border=True)
            col_a, col_b, col_c = st.columns(3)

            # Card 1
            with col_a:
                card1 = st.container(border=True)
                col1, col2 = st.columns(2)
                with card1:
                    with col1:
                        st.image('https://static.streamlit.io/examples/cat.jpg')

                    # Pricing
                    with col2:
                        st.metric('Current Market Price', '$12.05', '$0.05')

                # Additional card details
                card_details = st.container()
                with card_details:
                    st.text('Set: ')
                    st.text('Rarity: ')
                    st.text('Title: ')

            # Card 2
            with col_b:
                card2 = st.container(border=True)
                col3, col4 = st.columns(2)
                with card2:
                    with col3:
                        st.image('https://static.streamlit.io/examples/cat.jpg')

                    # Pricing
                    with col4:
                        st.metric('Current Market Price', '$12.05', '$0.05')
                
                # Additional card details
                card_details = st.container()
                with card_details:
                    st.text('Set: ')
                    st.text('Rarity: ')
                    st.text('Title: ')

            # Card 3
            with col_c:
                card3 = st.container(border=True)
                col5, col6 = st.columns(2)
                with card3:
                    with col5:
                        st.image('https://static.streamlit.io/examples/cat.jpg')

                    # Pricing
                    with col6:
                        st.metric('Current Market Price', '$12.05', '$0.05')

                # Additional card details
                card_details = st.container()
                with card_details:
                    st.text('Set: ')
                    st.text('Rarity: ')
                    st.text('Title: ')


            # Table 
            table_container = st.container()
            with table_container:
                df = pd.DataFrame(
                    {
                                "name": ["Roadmap", "Extras", "Issues"],
                                "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
                                "stars": [random.randint(0, 1000) for _ in range(3)],
                                "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
                            
                    }
                    
                )
                st.dataframe(
                    df,
                    column_config={
                        "name": "App name", 
                        "stars": st.column_config.NumberColumn(
                            "Github Stars",
                            help="Number of stars on GitHub",
                            format="%d ⭐",
                        ),
                        "url": st.column_config.LinkColumn("App URL"),
                        "views_history": st.column_config.LineChartColumn(
                            "Views (past 30 days)", y_min=0, y_max=5000
                        ),
                    },
                    hide_index=True,
                    use_container_width=True,
                )


    def create_yugioh_tab(self):
        with self.tab2:
            st.text('Last Updated: ')
            # Trending cards
            top_3 = st.container(border=True)
            col_a, col_b, col_c = st.columns(3)

            # Card 1
            with col_a:
                card1 = st.container(border=True)
                col1, col2 = st.columns(2)
                with card1:
                    with col1:
                        st.image('https://static.streamlit.io/examples/cat.jpg')

                    # Pricing
                    with col2:
                        st.metric('Current Market Price', '$12.05', '$0.05')

                # Additional card details
                card_details = st.container()
                with card_details:
                    st.text('Set: ')
                    st.text('Rarity: ')
                    st.text('Title: ')

            # Card 2
            with col_b:
                card2 = st.container(border=True)
                col3, col4 = st.columns(2)
                with card2:
                    with col3:
                        st.image('https://static.streamlit.io/examples/cat.jpg')

                    # Pricing
                    with col4:
                        st.metric('Current Market Price', '$12.05', '$0.05')
                
                # Additional card details
                card_details = st.container()
                with card_details:
                    st.text('Set: ')
                    st.text('Rarity: ')
                    st.text('Title: ')

            # Card 3
            with col_c:
                card3 = st.container(border=True)
                col5, col6 = st.columns(2)
                with card3:
                    with col5:
                        st.image('https://static.streamlit.io/examples/cat.jpg')

                    # Pricing
                    with col6:
                        st.metric('Current Market Price', '$12.05', '$0.05')

                # Additional card details
                card_details = st.container()
                with card_details:
                    st.text('Set: ')
                    st.text('Rarity: ')
                    st.text('Title: ')


            # Table 
            table_container = st.container()
            with table_container:
                df = pd.DataFrame(
                    {
                                "name": ["Roadmap", "Extras", "Issues"],
                                "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
                                "stars": [random.randint(0, 1000) for _ in range(3)],
                                "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
                            
                    }
                    
                )
                st.dataframe(
                    df,
                    column_config={
                        "name": "App name", 
                        "stars": st.column_config.NumberColumn(
                            "Github Stars",
                            help="Number of stars on GitHub",
                            format="%d ⭐",
                        ),
                        "url": st.column_config.LinkColumn("App URL"),
                        "views_history": st.column_config.LineChartColumn(
                            "Views (past 30 days)", y_min=0, y_max=5000
                        ),
                    },
                    hide_index=True,
                    use_container_width=True,
                )



def main():
    tcg = TCGPlayerData()
    tcg.create_one_piece_tab()
    tcg.create_yugioh_tab()

    url = "https://api.tcgplayer.com/app/authorize/authCode"

    headers = {"accept": "application/json"}

    response = requests.post(url, headers=headers)

    print(response.text)




if __name__ == '__main__':
    main()

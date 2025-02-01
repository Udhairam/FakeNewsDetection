'''{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-xLUTcYdhxKc",
        "outputId": "19f2c5c5-2ea2-4686-cbef-78cd145aa9aa"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "goA61-YZhDa1"
      },
      "outputs": [],
      "source": [
        "import pandas as pd"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qKpJg5EIhDa9"
      },
      "outputs": [],
      "source": [
        "df=pd.read_csv('/content/drive/MyDrive/Final_year_proj/train.csv')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "821KJnychDa-",
        "outputId": "87b49f0d-3624-4627-9dea-0dfe7b5a1ebe"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   id                                              title              author  \\\n",
              "0   0  House Dem Aide: We Didn’t Even See Comey’s Let...       Darrell Lucus   \n",
              "1   1  FLYNN: Hillary Clinton, Big Woman on Campus - ...     Daniel J. Flynn   \n",
              "2   2                  Why the Truth Might Get You Fired  Consortiumnews.com   \n",
              "3   3  15 Civilians Killed In Single US Airstrike Hav...     Jessica Purkiss   \n",
              "4   4  Iranian woman jailed for fictional unpublished...      Howard Portnoy   \n",
              "\n",
              "                                                text  label  \n",
              "0  House Dem Aide: We Didn’t Even See Comey’s Let...      1  \n",
              "1  Ever get the feeling your life circles the rou...      0  \n",
              "2  Why the Truth Might Get You Fired October 29, ...      1  \n",
              "3  Videos 15 Civilians Killed In Single US Airstr...      1  \n",
              "4  Print \\nAn Iranian woman has been sentenced to...      1  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-951d4a3b-f064-47b7-9404-249cebc597d0\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id</th>\n",
              "      <th>title</th>\n",
              "      <th>author</th>\n",
              "      <th>text</th>\n",
              "      <th>label</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>House Dem Aide: We Didn’t Even See Comey’s Let...</td>\n",
              "      <td>Darrell Lucus</td>\n",
              "      <td>House Dem Aide: We Didn’t Even See Comey’s Let...</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>FLYNN: Hillary Clinton, Big Woman on Campus - ...</td>\n",
              "      <td>Daniel J. Flynn</td>\n",
              "      <td>Ever get the feeling your life circles the rou...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2</td>\n",
              "      <td>Why the Truth Might Get You Fired</td>\n",
              "      <td>Consortiumnews.com</td>\n",
              "      <td>Why the Truth Might Get You Fired October 29, ...</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>3</td>\n",
              "      <td>15 Civilians Killed In Single US Airstrike Hav...</td>\n",
              "      <td>Jessica Purkiss</td>\n",
              "      <td>Videos 15 Civilians Killed In Single US Airstr...</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>4</td>\n",
              "      <td>Iranian woman jailed for fictional unpublished...</td>\n",
              "      <td>Howard Portnoy</td>\n",
              "      <td>Print \\nAn Iranian woman has been sentenced to...</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-951d4a3b-f064-47b7-9404-249cebc597d0')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-951d4a3b-f064-47b7-9404-249cebc597d0 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-951d4a3b-f064-47b7-9404-249cebc597d0');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ],
      "source": [
        "df.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "hy8hJUqfhDa_"
      },
      "outputs": [],
      "source": [
        "X=df.drop('label',axis=1)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "LBQBA1wzhDa_",
        "outputId": "98e81a1e-129d-4600-ce4f-918f3ea6a36f"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   id                                              title              author  \\\n",
              "0   0  House Dem Aide: We Didn’t Even See Comey’s Let...       Darrell Lucus   \n",
              "1   1  FLYNN: Hillary Clinton, Big Woman on Campus - ...     Daniel J. Flynn   \n",
              "2   2                  Why the Truth Might Get You Fired  Consortiumnews.com   \n",
              "3   3  15 Civilians Killed In Single US Airstrike Hav...     Jessica Purkiss   \n",
              "4   4  Iranian woman jailed for fictional unpublished...      Howard Portnoy   \n",
              "\n",
              "                                                text  \n",
              "0  House Dem Aide: We Didn’t Even See Comey’s Let...  \n",
              "1  Ever get the feeling your life circles the rou...  \n",
              "2  Why the Truth Might Get You Fired October 29, ...  \n",
              "3  Videos 15 Civilians Killed In Single US Airstr...  \n",
              "4  Print \\nAn Iranian woman has been sentenced to...  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e0a135e5-3a40-4685-ba2b-06d66a3a77e9\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id</th>\n",
              "      <th>title</th>\n",
              "      <th>author</th>\n",
              "      <th>text</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>House Dem Aide: We Didn’t Even See Comey’s Let...</td>\n",
              "      <td>Darrell Lucus</td>\n",
              "      <td>House Dem Aide: We Didn’t Even See Comey’s Let...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>FLYNN: Hillary Clinton, Big Woman on Campus - ...</td>\n",
              "      <td>Daniel J. Flynn</td>\n",
              "      <td>Ever get the feeling your life circles the rou...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2</td>\n",
              "      <td>Why the Truth Might Get You Fired</td>\n",
              "      <td>Consortiumnews.com</td>\n",
              "      <td>Why the Truth Might Get You Fired October 29, ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>3</td>\n",
              "      <td>15 Civilians Killed In Single US Airstrike Hav...</td>\n",
              "      <td>Jessica Purkiss</td>\n",
              "      <td>Videos 15 Civilians Killed In Single US Airstr...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>4</td>\n",
              "      <td>Iranian woman jailed for fictional unpublished...</td>\n",
              "      <td>Howard Portnoy</td>\n",
              "      <td>Print \\nAn Iranian woman has been sentenced to...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e0a135e5-3a40-4685-ba2b-06d66a3a77e9')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-e0a135e5-3a40-4685-ba2b-06d66a3a77e9 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-e0a135e5-3a40-4685-ba2b-06d66a3a77e9');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ],
      "source": [
        "X.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "c0fWmAJthDbA"
      },
      "outputs": [],
      "source": [
        "y=df['label']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ftiX8Z4yhDbA",
        "outputId": "69ae5b51-e813-430b-f79e-7da38b65c9c7"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    1\n",
              "1    0\n",
              "2    1\n",
              "3    1\n",
              "4    1\n",
              "Name: label, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ],
      "source": [
        "y.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GsO5CdljhDbA",
        "outputId": "753fd13d-082f-4599-8e2d-f6552b86b4cc"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(20800, 5)"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ],
      "source": [
        "df.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "rvz9rmB7hDbB"
      },
      "outputs": [],
      "source": [
        "from sklearn.feature_extraction.text import TfidfVectorizer"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "oLpu_Y6xhDbB"
      },
      "outputs": [],
      "source": [
        "df=df.dropna()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "oqmWqIcKhDbB"
      },
      "outputs": [],
      "source": [
        "messages=df.copy()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "2pWuSWkBhDbC"
      },
      "outputs": [],
      "source": [
        "messages.reset_index(inplace=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 363
        },
        "id": "LyGPrM8ZhDbC",
        "outputId": "30fad8f8-6b9b-4aeb-dc96-64fe4497d026"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   index  id                                              title  \\\n",
              "0      0   0  House Dem Aide: We Didn’t Even See Comey’s Let...   \n",
              "1      1   1  FLYNN: Hillary Clinton, Big Woman on Campus - ...   \n",
              "2      2   2                  Why the Truth Might Get You Fired   \n",
              "3      3   3  15 Civilians Killed In Single US Airstrike Hav...   \n",
              "4      4   4  Iranian woman jailed for fictional unpublished...   \n",
              "5      5   5  Jackie Mason: Hollywood Would Love Trump if He...   \n",
              "6      7   7  Benoît Hamon Wins French Socialist Party’s Pre...   \n",
              "7      9   9  A Back-Channel Plan for Ukraine and Russia, Co...   \n",
              "8     10  10  Obama’s Organizing for Action Partners with So...   \n",
              "9     11  11  BBC Comedy Sketch \"Real Housewives of ISIS\" Ca...   \n",
              "\n",
              "                         author  \\\n",
              "0                 Darrell Lucus   \n",
              "1               Daniel J. Flynn   \n",
              "2            Consortiumnews.com   \n",
              "3               Jessica Purkiss   \n",
              "4                Howard Portnoy   \n",
              "5               Daniel Nussbaum   \n",
              "6               Alissa J. Rubin   \n",
              "7  Megan Twohey and Scott Shane   \n",
              "8                   Aaron Klein   \n",
              "9               Chris Tomlinson   \n",
              "\n",
              "                                                text  label  \n",
              "0  House Dem Aide: We Didn’t Even See Comey’s Let...      1  \n",
              "1  Ever get the feeling your life circles the rou...      0  \n",
              "2  Why the Truth Might Get You Fired October 29, ...      1  \n",
              "3  Videos 15 Civilians Killed In Single US Airstr...      1  \n",
              "4  Print \\nAn Iranian woman has been sentenced to...      1  \n",
              "5  In these trying times, Jackie Mason is the Voi...      0  \n",
              "6  PARIS  —   France chose an idealistic, traditi...      0  \n",
              "7  A week before Michael T. Flynn resigned as nat...      0  \n",
              "8  Organizing for Action, the activist group that...      0  \n",
              "9  The BBC produced spoof on the “Real Housewives...      0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a2de4e93-0cd6-4127-9976-52ba63dce970\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>index</th>\n",
              "      <th>id</th>\n",
              "      <th>title</th>\n",
              "      <th>author</th>\n",
              "      <th>text</th>\n",
              "      <th>label</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>House Dem Aide: We Didn’t Even See Comey’s Let...</td>\n",
              "      <td>Darrell Lucus</td>\n",
              "      <td>House Dem Aide: We Didn’t Even See Comey’s Let...</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>FLYNN: Hillary Clinton, Big Woman on Campus - ...</td>\n",
              "      <td>Daniel J. Flynn</td>\n",
              "      <td>Ever get the feeling your life circles the rou...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>Why the Truth Might Get You Fired</td>\n",
              "      <td>Consortiumnews.com</td>\n",
              "      <td>Why the Truth Might Get You Fired October 29, ...</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>15 Civilians Killed In Single US Airstrike Hav...</td>\n",
              "      <td>Jessica Purkiss</td>\n",
              "      <td>Videos 15 Civilians Killed In Single US Airstr...</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>Iranian woman jailed for fictional unpublished...</td>\n",
              "      <td>Howard Portnoy</td>\n",
              "      <td>Print \\nAn Iranian woman has been sentenced to...</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>5</td>\n",
              "      <td>5</td>\n",
              "      <td>Jackie Mason: Hollywood Would Love Trump if He...</td>\n",
              "      <td>Daniel Nussbaum</td>\n",
              "      <td>In these trying times, Jackie Mason is the Voi...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>7</td>\n",
              "      <td>7</td>\n",
              "      <td>Benoît Hamon Wins French Socialist Party’s Pre...</td>\n",
              "      <td>Alissa J. Rubin</td>\n",
              "      <td>PARIS  —   France chose an idealistic, traditi...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>9</td>\n",
              "      <td>9</td>\n",
              "      <td>A Back-Channel Plan for Ukraine and Russia, Co...</td>\n",
              "      <td>Megan Twohey and Scott Shane</td>\n",
              "      <td>A week before Michael T. Flynn resigned as nat...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>10</td>\n",
              "      <td>10</td>\n",
              "      <td>Obama’s Organizing for Action Partners with So...</td>\n",
              "      <td>Aaron Klein</td>\n",
              "      <td>Organizing for Action, the activist group that...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>11</td>\n",
              "      <td>11</td>\n",
              "      <td>BBC Comedy Sketch \"Real Housewives of ISIS\" Ca...</td>\n",
              "      <td>Chris Tomlinson</td>\n",
              "      <td>The BBC produced spoof on the “Real Housewives...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a2de4e93-0cd6-4127-9976-52ba63dce970')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-a2de4e93-0cd6-4127-9976-52ba63dce970 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-a2de4e93-0cd6-4127-9976-52ba63dce970');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ],
      "source": [
        "messages.head(10)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 123
        },
        "id": "jpS8rNoHhDbC",
        "outputId": "b186d4bd-3d63-4fd3-fc3d-02018597566c"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'PARIS  —   France chose an idealistic, traditional   candidate in Sunday’s primary to represent the Socialist and   parties in the presidential election this spring. The candidate, Benoît Hamon, 49, who ran on the slogan that he would “make France’s heart beat,” bested Manuel Valls, the former prime minister, whose campaign has promoted more   policies and who has a strong    background. Mr. Hamon appeared to have won by a wide margin, with incomplete returns showing him with an estimated 58 percent of the vote to Mr. Valls’s 41 percent. “Tonight the left holds its head up high again it is looking to the future,” Mr. Hamon said, addressing his supporters. “Our country needs the left, but a modern, innovative left,” he said. Mr. Hamon’s victory was the clearest sign yet that voters on the left want a break with the policies of President François Hollande, who in December announced that he would not seek  . However, Mr. Hamon’s strong showing is unlikely to change widespread assessments that   candidates have little chance of making it into the second round of voting in the general election. The first round of the general election is set for April 23 and the runoff for May 7. The Socialist Party is deeply divided, and one measure of its lack of popular enthusiasm was the relatively low number of people voting. About two million people voted in the second round of the primary on Sunday, in contrast with about 2. 9 million in the second round of the last presidential primary on the left, in 2011. However, much of the conventional wisdom over how the elections will go has been thrown into question over the past week, because the leading candidate, François Fillon, who represents the main   party, the Republicans, was accused of paying his wife large sums of money to work as his parliamentary aide. While nepotism is legal in the French political system, it is not clear that she actually did any work. Prosecutors who specialize in financial malfeasance are reviewing the case. France’s electoral system allows multiple candidates to run for president in the first round of voting, but only the top two   go on to a second round. Mr. Hamon is entering a race that is already crowded on the left, with candidates who include   Mélenchon on the far left, and Emmanuel Macron, an independent who served as economy minister in Mr. Hollande’s government and who embraces more   policies. Unless he decides to withdraw, Mr. Fillon, the mainstream right candidate, will also run, as will the extreme right candidate Marine Le Pen. The two have been expected to go to the runoff. Mr. Hamon’s victory can be attributed at least in part to his image as an idealist and traditional leftist candidate who appeals to union voters as well as more environmentally concerned and socially liberal young people. Unlike Mr. Valls, he also clearly distanced himself from some of Mr. Hollande’s more unpopular policies, especially the economic ones. Thomas Kekenbosch, 22, a student and one of the leaders of the group the Youth With Benoît Hamon, said Mr. Hamon embodied a new hope for those on the left. “We have a perspective we have something to do, to build,” Mr. Kekenbosch said. Mr. Hollande had disappointed many young people because under him the party abandoned ideals, such as support for workers, that many   voters believe in, according to Mr. Kekenbosch. Mr. Hollande’s government, under pressure from the European Union to meet budget restraints, struggled to pass labor code reforms to make the market more attractive to foreign investors and also to encourage French businesses to expand in France. The measures ultimately passed after weeks of strikes, but they were watered down and generated little concrete progress in improving France’s roughly 10 percent unemployment rate and its nearly 25 percent youth joblessness rate. Mr. Hamon strongly endorses a stimulus approach to improving the economy and has promised to phase in a universal income, which would especially help young people looking for work, but would also supplement the livelihood of   French workers. The end goal would be to have everyone receive 750 euros per month (about $840). “We have someone that trusts us,” Mr. Kekenbosch said, “who says: ‘I give you enough to pay for your studies. You can have a scholarship which spares you from working at McDonald’s on provisional contracts for 4 years. ” Mr. Hamon advocates phasing out diesel fuel and encouraging drivers to replace vehicles that use petroleum products with electrical ones. His leftist pedigree began early. His father worked at an arsenal in Brest, a city in the far west of Brittany, and his mother worked off and on as a secretary. He was an early member of the Movement of Young Socialists, and he has continued to work closely with them through his political life. He also worked for Martine Aubry, now the mayor of Lille and a former Socialist Party leader.'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 15
        }
      ],
      "source": [
        "messages['text'][6]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y3x7FVzshDbC",
        "outputId": "14c53c65-92c7-41d1-af6d-b6c3b5920433"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package stopwords to /root/nltk_data...\n",
            "[nltk_data]   Unzipping corpora/stopwords.zip.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['i',\n",
              " 'me',\n",
              " 'my',\n",
              " 'myself',\n",
              " 'we',\n",
              " 'our',\n",
              " 'ours',\n",
              " 'ourselves',\n",
              " 'you',\n",
              " \"you're\",\n",
              " \"you've\",\n",
              " \"you'll\",\n",
              " \"you'd\",\n",
              " 'your',\n",
              " 'yours',\n",
              " 'yourself',\n",
              " 'yourselves',\n",
              " 'he',\n",
              " 'him',\n",
              " 'his',\n",
              " 'himself',\n",
              " 'she',\n",
              " \"she's\",\n",
              " 'her',\n",
              " 'hers',\n",
              " 'herself',\n",
              " 'it',\n",
              " \"it's\",\n",
              " 'its',\n",
              " 'itself',\n",
              " 'they',\n",
              " 'them',\n",
              " 'their',\n",
              " 'theirs',\n",
              " 'themselves',\n",
              " 'what',\n",
              " 'which',\n",
              " 'who',\n",
              " 'whom',\n",
              " 'this',\n",
              " 'that',\n",
              " \"that'll\",\n",
              " 'these',\n",
              " 'those',\n",
              " 'am',\n",
              " 'is',\n",
              " 'are',\n",
              " 'was',\n",
              " 'were',\n",
              " 'be',\n",
              " 'been',\n",
              " 'being',\n",
              " 'have',\n",
              " 'has',\n",
              " 'had',\n",
              " 'having',\n",
              " 'do',\n",
              " 'does',\n",
              " 'did',\n",
              " 'doing',\n",
              " 'a',\n",
              " 'an',\n",
              " 'the',\n",
              " 'and',\n",
              " 'but',\n",
              " 'if',\n",
              " 'or',\n",
              " 'because',\n",
              " 'as',\n",
              " 'until',\n",
              " 'while',\n",
              " 'of',\n",
              " 'at',\n",
              " 'by',\n",
              " 'for',\n",
              " 'with',\n",
              " 'about',\n",
              " 'against',\n",
              " 'between',\n",
              " 'into',\n",
              " 'through',\n",
              " 'during',\n",
              " 'before',\n",
              " 'after',\n",
              " 'above',\n",
              " 'below',\n",
              " 'to',\n",
              " 'from',\n",
              " 'up',\n",
              " 'down',\n",
              " 'in',\n",
              " 'out',\n",
              " 'on',\n",
              " 'off',\n",
              " 'over',\n",
              " 'under',\n",
              " 'again',\n",
              " 'further',\n",
              " 'then',\n",
              " 'once',\n",
              " 'here',\n",
              " 'there',\n",
              " 'when',\n",
              " 'where',\n",
              " 'why',\n",
              " 'how',\n",
              " 'all',\n",
              " 'any',\n",
              " 'both',\n",
              " 'each',\n",
              " 'few',\n",
              " 'more',\n",
              " 'most',\n",
              " 'other',\n",
              " 'some',\n",
              " 'such',\n",
              " 'no',\n",
              " 'nor',\n",
              " 'not',\n",
              " 'only',\n",
              " 'own',\n",
              " 'same',\n",
              " 'so',\n",
              " 'than',\n",
              " 'too',\n",
              " 'very',\n",
              " 's',\n",
              " 't',\n",
              " 'can',\n",
              " 'will',\n",
              " 'just',\n",
              " 'don',\n",
              " \"don't\",\n",
              " 'should',\n",
              " \"should've\",\n",
              " 'now',\n",
              " 'd',\n",
              " 'll',\n",
              " 'm',\n",
              " 'o',\n",
              " 're',\n",
              " 've',\n",
              " 'y',\n",
              " 'ain',\n",
              " 'aren',\n",
              " \"aren't\",\n",
              " 'couldn',\n",
              " \"couldn't\",\n",
              " 'didn',\n",
              " \"didn't\",\n",
              " 'doesn',\n",
              " \"doesn't\",\n",
              " 'hadn',\n",
              " \"hadn't\",\n",
              " 'hasn',\n",
              " \"hasn't\",\n",
              " 'haven',\n",
              " \"haven't\",\n",
              " 'isn',\n",
              " \"isn't\",\n",
              " 'ma',\n",
              " 'mightn',\n",
              " \"mightn't\",\n",
              " 'mustn',\n",
              " \"mustn't\",\n",
              " 'needn',\n",
              " \"needn't\",\n",
              " 'shan',\n",
              " \"shan't\",\n",
              " 'shouldn',\n",
              " \"shouldn't\",\n",
              " 'wasn',\n",
              " \"wasn't\",\n",
              " 'weren',\n",
              " \"weren't\",\n",
              " 'won',\n",
              " \"won't\",\n",
              " 'wouldn',\n",
              " \"wouldn't\"]"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ],
      "source": [
        "import nltk\n",
        "nltk.download('stopwords')\n",
        "from nltk.corpus import stopwords\n",
        "stopwords.words('english')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6QcYn9UpIz9u"
      },
      "source": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "YN2jDtFEhDbD"
      },
      "outputs": [],
      "source": [
        "from nltk.corpus import stopwords\n",
        "from nltk.stem.porter import PorterStemmer\n",
        "import re\n",
        "ps = PorterStemmer()\n",
        "corpus = []\n",
        "for i in range(0, len(messages)):\n",
        "    review = re.sub('[^a-zA-Z]', ' ', messages['text'][i])\n",
        "    review = review.lower()\n",
        "    review = review.split()\n",
        "\n",
        "    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]\n",
        "    review = ' '.join(review)\n",
        "    corpus.append(review)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 123
        },
        "id": "A2QsEEMehDbD",
        "outputId": "1b056773-3002-47b3-f011-78c90d52ecc3"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'video civilian kill singl us airstrik identifi rate civilian kill american airstrik afghanistan higher us engag activ combat oper photo hellfir missil load onto us militari reaper drone afghanistan staff sgt brian ferguson u air forc bureau abl identifi civilian kill singl us drone strike afghanistan last month biggest loss civilian life one strike sinc attack medecin san frontier hospit msf last octob us claim conduct counter terror strike islam state fighter hit nangarhar provinc missil septemb next day unit nation issu unusu rapid strong statement say strike kill civilian injur other gather hous celebr tribal elder return pilgrimag mecca bureau spoke man name haji rai said owner hous target said peopl kill other injur provid name list bureau abl independ verifi ident die rai son headmast local school among anoth man abdul hakim lost three son attack rai said involv deni us claim member visit hous strike said even speak sort peopl phone let alon receiv hous death amount biggest confirm loss civilian life singl american strike afghanistan sinc attack msf hospit kunduz last octob kill least peopl nangarhar strike us attack kill civilian septemb bureau data indic mani civilian alli soldier kill four american strike afghanistan somalia month septemb pair strike kill eight afghan policemen tarinkot capit urozgan provic us jet reportedli hit polic checkpoint kill one offic return target first respond use tactic known doubl tap strike controversi often hit civilian rescuer us told bureau conduct strike individu fire pose threat afghan forc email directli address alleg afghan policemen kill end month somalia citizen burnt us flag street north central citi galcayo emerg drone attack may unintent kill somali soldier civilian strike occur day one nangarhar somali afghan incid us first deni non combat kill investig strike nangarhar galcayo rate civilian kill american airstrik afghanistan higher us engag activ combat oper name'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 18
        }
      ],
      "source": [
        "corpus[3]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "0N-NOZKPhDbD"
      },
      "outputs": [],
      "source": [
        "from sklearn.feature_extraction.text import TfidfVectorizer\n",
        "tfidf_v=TfidfVectorizer(max_features=5000,ngram_range=(1,3))\n",
        "X=tfidf_v.fit_transform(corpus).toarray()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RWzKpJwghDbE",
        "outputId": "aac8bf5b-2217-492a-fc2b-40d7dff30570"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(18285, 5000)"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ],
      "source": [
        "X.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "p3GMgF9ahDbE"
      },
      "outputs": [],
      "source": [
        "y=messages['label']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Ao21Ke4JhDbE"
      },
      "outputs": [],
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "sf1A31QMPv0P"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gLmtjQg-hDbE",
        "outputId": "7e5d361f-c9d5-4925-80e0-dc8e700a0fed"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'analyzer': 'word',\n",
              " 'binary': False,\n",
              " 'decode_error': 'strict',\n",
              " 'dtype': numpy.float64,\n",
              " 'encoding': 'utf-8',\n",
              " 'input': 'content',\n",
              " 'lowercase': True,\n",
              " 'max_df': 1.0,\n",
              " 'max_features': 5000,\n",
              " 'min_df': 1,\n",
              " 'ngram_range': (1, 3),\n",
              " 'norm': 'l2',\n",
              " 'preprocessor': None,\n",
              " 'smooth_idf': True,\n",
              " 'stop_words': None,\n",
              " 'strip_accents': None,\n",
              " 'sublinear_tf': False,\n",
              " 'token_pattern': '(?u)\\\\b\\\\w\\\\w+\\\\b',\n",
              " 'tokenizer': None,\n",
              " 'use_idf': True,\n",
              " 'vocabulary': None}"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ],
      "source": [
        "tfidf_v.get_params()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "g9Qd-SyvhDbF"
      },
      "outputs": [],
      "source": [
        "# count_df = pd.DataFrame(X_train, columns=tfidf_v.get_feature_names())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Sp_i-x_FhDbF"
      },
      "outputs": [],
      "source": [
        "# count_df.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "D4-cz3_HhDbF"
      },
      "outputs": [],
      "source": [
        "import matplotlib.pyplot as plt"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "5Hdsg4AIhDbF"
      },
      "outputs": [],
      "source": [
        "def plot_confusion_matrix(cm, classes,\n",
        "                          normalize=False,\n",
        "                          title='Confusion matrix',\n",
        "                          cmap=plt.cm.Blues):\n",
        "    plt.imshow(cm, interpolation='nearest', cmap=cmap)\n",
        "    plt.title(title)\n",
        "    plt.colorbar()\n",
        "    tick_marks = np.arange(len(classes))\n",
        "    plt.xticks(tick_marks, classes, rotation=45)\n",
        "    plt.yticks(tick_marks, classes)\n",
        "\n",
        "    if normalize:\n",
        "        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]\n",
        "        print(\"Normalized confusion matrix\")\n",
        "    else:\n",
        "        print('Confusion matrix, without normalization')\n",
        "\n",
        "    thresh = cm.max() / 2.\n",
        "    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):\n",
        "        plt.text(j, i, cm[i, j],\n",
        "                 horizontalalignment=\"center\",\n",
        "                 color=\"white\" if cm[i, j] > thresh else \"black\")\n",
        "\n",
        "    plt.tight_layout()\n",
        "    plt.ylabel('True label')\n",
        "    plt.xlabel('Predicted label')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 182
        },
        "id": "Ppumh94PhDbG",
        "outputId": "38dbcfe7-1ee4-4e58-8326-3af108e6aa4f"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-31-f2f55e1e1dbe>\u001b[0m in \u001b[0;36m<cell line: 2>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlinear_model\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mPassiveAggressiveClassifier\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mlinear_clf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mPassiveAggressiveClassifier\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m50\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: PassiveAggressiveClassifier.__init__() takes 1 positional argument but 2 were given"
          ]
        }
      ],
      "source": [
        "from sklearn.linear_model import PassiveAggressiveClassifier\n",
        "linear_clf = PassiveAggressiveClassifier(50)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "CUGMm4DIpxWz"
      },
      "outputs": [],
      "source": [
        "from sklearn import metrics\n",
        "import numpy as np\n",
        "import itertools"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 235
        },
        "id": "C4493GeAhDbG",
        "outputId": "438c852f-d1de-4133-8983-04290544a12a"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-33-0e1669fd241b>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mlinear_clf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX_train\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my_train\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mpred\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mlinear_clf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpredict\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX_test\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mscore\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmetrics\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0maccuracy_score\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0my_test\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpred\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"accuracy:   %0.3f\"\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0mscore\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmetrics\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconfusion_matrix\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0my_test\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpred\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'linear_clf' is not defined"
          ]
        }
      ],
      "source": [
        "linear_clf.fit(X_train, y_train)\n",
        "pred = linear_clf.predict(X_test)\n",
        "score = metrics.accuracy_score(y_test, pred)\n",
        "print(\"accuracy:   %0.3f\" % score)\n",
        "cm = metrics.confusion_matrix(y_test, pred)\n",
        "plot_confusion_matrix(cm, classes=['FAKE Data', 'REAL Data'])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "0cH4VGBMp7pr"
      },
      "outputs": [],
      "source": [
        "td=pd.read_csv('/content/drive/MyDrive/Final_year_proj/test.csv')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "bVRj5x2rp1iW",
        "outputId": "69d9ca0e-9dac-47d1-c03a-24cc8e5a0154"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      id                                              title  \\\n",
              "0  20800  Specter of Trump Loosens Tongues, if Not Purse...   \n",
              "1  20801  Russian warships ready to strike terrorists ne...   \n",
              "2  20802  #NoDAPL: Native American Leaders Vow to Stay A...   \n",
              "3  20803  Tim Tebow Will Attempt Another Comeback, This ...   \n",
              "4  20804                    Keiser Report: Meme Wars (E995)   \n",
              "\n",
              "                    author                                               text  \n",
              "0         David Streitfeld  PALO ALTO, Calif.  —   After years of scorning...  \n",
              "1                      NaN  Russian warships ready to strike terrorists ne...  \n",
              "2            Common Dreams  Videos #NoDAPL: Native American Leaders Vow to...  \n",
              "3            Daniel Victor  If at first you don’t succeed, try a different...  \n",
              "4  Truth Broadcast Network  42 mins ago 1 Views 0 Comments 0 Likes 'For th...  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-d25c2be5-059f-469c-8d0e-57bea0dfe14d\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id</th>\n",
              "      <th>title</th>\n",
              "      <th>author</th>\n",
              "      <th>text</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>20800</td>\n",
              "      <td>Specter of Trump Loosens Tongues, if Not Purse...</td>\n",
              "      <td>David Streitfeld</td>\n",
              "      <td>PALO ALTO, Calif.  —   After years of scorning...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>20801</td>\n",
              "      <td>Russian warships ready to strike terrorists ne...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Russian warships ready to strike terrorists ne...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>20802</td>\n",
              "      <td>#NoDAPL: Native American Leaders Vow to Stay A...</td>\n",
              "      <td>Common Dreams</td>\n",
              "      <td>Videos #NoDAPL: Native American Leaders Vow to...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>20803</td>\n",
              "      <td>Tim Tebow Will Attempt Another Comeback, This ...</td>\n",
              "      <td>Daniel Victor</td>\n",
              "      <td>If at first you don’t succeed, try a different...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>20804</td>\n",
              "      <td>Keiser Report: Meme Wars (E995)</td>\n",
              "      <td>Truth Broadcast Network</td>\n",
              "      <td>42 mins ago 1 Views 0 Comments 0 Likes 'For th...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-d25c2be5-059f-469c-8d0e-57bea0dfe14d')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-d25c2be5-059f-469c-8d0e-57bea0dfe14d button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-d25c2be5-059f-469c-8d0e-57bea0dfe14d');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 36
        }
      ],
      "source": [
        "td.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JJC-8zfxq4k7",
        "outputId": "97839a30-a699-48fe-c63c-5efeebc67964"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(5200, 4)"
            ]
          },
          "metadata": {},
          "execution_count": 37
        }
      ],
      "source": [
        "td.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qNWlBPDfqsjJ"
      },
      "outputs": [],
      "source": [
        "td=td.dropna()\n",
        "td.reset_index(inplace=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EGG98NAmq-7g",
        "outputId": "dc107c1c-a9fc-429a-f445-789fa346f8d8"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(4575, 5)"
            ]
          },
          "metadata": {},
          "execution_count": 39
        }
      ],
      "source": [
        "td.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "1aLaYmvKrCWr"
      },
      "outputs": [],
      "source": [
        "from nltk.corpus import stopwords\n",
        "from nltk.stem.porter import PorterStemmer\n",
        "import re\n",
        "ps = PorterStemmer()\n",
        "corpus = []\n",
        "for i in range(0, len(td)):\n",
        "    review = re.sub('[^a-zA-Z]', ' ', td['text'][i])\n",
        "    review = review.lower()\n",
        "    review = review.split()\n",
        "\n",
        "    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]\n",
        "    review = ' '.join(review)\n",
        "    corpus.append(review)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "g4sxsr6IP_lf"
      },
      "outputs": [],
      "source": [
        "from sklearn.feature_extraction.text import TfidfVectorizer\n",
        "tfidf_v=TfidfVectorizer(max_features=5000,ngram_range=(1,3))\n",
        "Test=tfidf_v.fit_transform(corpus).toarray()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 235
        },
        "id": "7t5WYIZJCtgg",
        "outputId": "188928e8-a4b7-4dd0-b906-e7a58549e265"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-42-b67367a73d33>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mres\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mlinear_clf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpredict\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mTest\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mres_col\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mtrue\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mfake\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mres\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m   \u001b[0;32mif\u001b[0m \u001b[0mres\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m==\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'linear_clf' is not defined"
          ]
        }
      ],
      "source": [
        "res=linear_clf.predict(Test)\n",
        "res_col=[]\n",
        "true,fake=0,0\n",
        "for i in range(len(res)):\n",
        "  if res[i]==1:\n",
        "    true+=1\n",
        "    res_col.append('True')\n",
        "  else:\n",
        "    fake+=1\n",
        "    res_col.append('Fake')\n",
        "td['Real/Fake']=res_col\n",
        "td"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 217
        },
        "id": "PLfp_B1wRu_E",
        "outputId": "e0f870bf-7b9c-4e88-c6df-193bd56e8495"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-43-2fdbed5059b7>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m plt.pie([fake*100/len(td),true*100/len(td)],labels = ['Fake','True'], explode = [0.05,0],colors=['red','blue'],autopct='%d%%',\n\u001b[0m\u001b[1;32m      2\u001b[0m         shadow=True, startangle=270)\n\u001b[1;32m      3\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlegend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshow\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'fake' is not defined"
          ]
        }
      ],
      "source": [
        "plt.pie([fake*100/len(td),true*100/len(td)],labels = ['Fake','True'], explode = [0.05,0],colors=['red','blue'],autopct='%d%%',\n",
        "        shadow=True, startangle=270)\n",
        "plt.legend()\n",
        "plt.show()"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8.5"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
'''

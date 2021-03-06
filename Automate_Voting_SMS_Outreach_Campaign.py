{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Automating Voting Campaign SMS Outreach",
      "provenance": [],
      "authorship_tag": "ABX9TyOg+cwCSY7o8aAidDCHkTox",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/joyloruth/Automate-Voting-Outreach-SMS-Campaign/blob/master/Automate_Voting_SMS_Outreach_Campaign.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NhDGiQ-WrJ6A",
        "outputId": "9763cf5b-91e3-46b5-8f1e-3d90f20c2697",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 190
        }
      },
      "source": [
        "pip install twilio"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: twilio in /usr/local/lib/python3.6/dist-packages (6.45.3)\n",
            "Requirement already satisfied: requests>=2.0.0; python_version >= \"3.0\" in /usr/local/lib/python3.6/dist-packages (from twilio) (2.23.0)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.6/dist-packages (from twilio) (1.15.0)\n",
            "Requirement already satisfied: PyJWT>=1.4.2 in /usr/local/lib/python3.6/dist-packages (from twilio) (1.7.1)\n",
            "Requirement already satisfied: pytz in /usr/local/lib/python3.6/dist-packages (from twilio) (2018.9)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.6/dist-packages (from requests>=2.0.0; python_version >= \"3.0\"->twilio) (1.24.3)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.6/dist-packages (from requests>=2.0.0; python_version >= \"3.0\"->twilio) (3.0.4)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.6/dist-packages (from requests>=2.0.0; python_version >= \"3.0\"->twilio) (2.10)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.6/dist-packages (from requests>=2.0.0; python_version >= \"3.0\"->twilio) (2020.6.20)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MvlzJDT-9vwg"
      },
      "source": [
        "from twilio.rest import Client"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Hs_g4Au0rhWo",
        "outputId": "e9dc0236-3120-4a55-c4e0-2486aa7a6979",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "pip install schedule"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: schedule in /usr/local/lib/python3.6/dist-packages (0.6.0)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DFM_v4UKKYcL"
      },
      "source": [
        "import schedule"
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4_YW14GTo9YL"
      },
      "source": [
        "import random"
      ],
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "y_N8I2j6wTHW"
      },
      "source": [
        "account_sid = \"AC8600bd69ea99494c576e6d361a8fb819\""
      ],
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yv7-yfcAxByM"
      },
      "source": [
        "auth_token = \"9a584ea4274f943f6915e5955d81b540\""
      ],
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3bnu0HC7xNUf"
      },
      "source": [
        "client = Client(account_sid, auth_token)"
      ],
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nQBX3E8Jrqge"
      },
      "source": [
        "call_to_action = [\n",
        "                  \"Make Your Voice Count!\" + \" Click the link to Register to Vote \" + \" https://www.usa.gov/register-to-vote\",\n",
        "                  \"Make Your Voice Count!\" + \" Click the link to Get Election Reminders \" + \" https://www.rockthevote.org/how-to-vote/get-election-reminders\"]\n"
      ],
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fIQVrwetxZLm"
      },
      "source": [
        "def go_vote():\n",
        "  client.messages.create(\n",
        "  to=\"+1615*******\",\n",
        "  from_=\"+14708237886\",\n",
        "  body=call_to_action[random.randint(0,len(call_to_action)-1)]\n",
        "    )\n",
        "  schedule.every().day.at(\"10:30\").do(go_vote,call_to_action)"
      ],
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wf7HDPPAWG-P"
      },
      "source": [
        "while True:\n",
        "  go_vote()"
      ],
      "execution_count": 14,
      "outputs": []
    }
  ]
}

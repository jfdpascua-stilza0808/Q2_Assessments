{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNo7kigCDOfgSVPZhCRDgJy",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/jfdpascua-stilza0808/Q2_FA1_Acacia_Pascua/blob/main/Pascua_ModularCalculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GEUJTGyK3EnO",
        "outputId": "4b32213d-b360-4873-f83d-0ae6a04d7ea2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Modular Calculator\n",
            "Enter first number:10\n",
            "Enter second number:5\n",
            "Choose operation:\n",
            "1 - Addition\n",
            "2 - Subtraction\n",
            "3 - Multiplication\n",
            "4 - Division\n",
            "Enter choice (1-4):1\n",
            "Result: 15.0\n"
          ]
        }
      ],
      "source": [
        "def add_numbers(num1, num2):\n",
        "  return num1 + num2\n",
        "\n",
        "def subtract_numbers(num1, num2):\n",
        "  return num1 - num2\n",
        "\n",
        "def multiply_numbers(num1, num2):\n",
        "  return num1 * num2\n",
        "\n",
        "def divide_numbers(num1, num2):\n",
        "  return num1 / num2\n",
        "\n",
        "print(\"Modular Calculator\")\n",
        "num1 = float(input(\"Enter first number:\"))\n",
        "num2 = float(input(\"Enter second number:\"))\n",
        "\n",
        "print(\"Choose operation:\")\n",
        "print(\"1 - Addition\")\n",
        "print(\"2 - Subtraction\")\n",
        "print(\"3 - Multiplication\")\n",
        "print(\"4 - Division\")\n",
        "choice = input(\"Enter choice (1-4):\")\n",
        "\n",
        "if choice == \"1\":\n",
        "  result = add_numbers(num1,num2)\n",
        "elif choice == \"2\":\n",
        "  result = subtract_numbers(num1,num2)\n",
        "elif choice == \"3\":\n",
        "  result = multiply_numbers(num1,num2)\n",
        "elif choice == \"4\":\n",
        "  result = divide_numbers(num1, num2)\n",
        "else:\n",
        "  result = \"Invalid Operation.\"\n",
        "\n",
        "print(f\"Result: {result}\")"
      ]
    }
  ]
}
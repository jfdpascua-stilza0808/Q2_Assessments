{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP5wcAy5uC5Sj/WvUUooQkK",
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
        "<a href=\"https://colab.research.google.com/github/jfdpascua-stilza0808/Q2_FA1_Acacia_Pascua/blob/main/Pascua_ModularCalculator_ver2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "DBWmxp82JF6R"
      },
      "outputs": [],
      "source": [
        "# Modular Calculator\n",
        "\n",
        "def add_numbers(num1, num2):\n",
        "  # Process: Add the two parameters\n",
        "  return num1 + num2\n",
        "\n",
        "def subtract_numbers(num1, num2):\n",
        "  # Process: Subtract num2 from num1\n",
        "  return num1 - num2\n",
        "\n",
        "def multiply_numbers(num1, num2):\n",
        "  # Process: Multiply the two parameters\n",
        "  return num1 * num2\n",
        "\n",
        "def divide_numbers(num1, num2):\n",
        "  # Process: Divide with zero check\n",
        "  if num2 == 0:\n",
        "    return \"Cannot divide by zero.\"\n",
        "  return num1 / num2\n",
        "\n",
        "# Main Program Flow\n",
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
        "# Store returned value in a variable\n",
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
        "# Display result clearly\n",
        "print(f\"Result: {result}\")"
      ]
    }
  ]
}
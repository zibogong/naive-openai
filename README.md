# NaiveOpenAI

## About
NaiveOpenAI is an open-source Python wrapper for the OpenAI API, specifically designed to aid entrepreneurs and B2B developers who utilize OpenAI's large language models (LLMs). It focuses on continuously iterating and enhancing product performance, thus offering a reliable tool for developers who need to showcase robust and reliable applications to investors and customers.

## Features
- **Degradation Simulation**: Includes a feature to simulate the degradation of the API's performance over time or under specific conditions. This is useful for testing how applications behave under less ideal conditions.
- **Customizable Degradation**: Allows users to set a degradation rate, providing flexibility in how significantly the model's performance is degraded.
- **Response Delay Handling**: Simulates increased response times based on the degradation rate, helping in testing application responsiveness under varying API response conditions.

## Installation
To use NaiveOpenAI in your project, you will need Python installed on your machine. Clone this repository and install it manually.

```bash
git clone git@github.com:zibogong/naive-openai.git
cd naive-openai
pip install .
```

## Usage
```python
from naiveopenai import NaiveOpenAI

# Initialize with degradation rate (0 means no degradation, 1 means full degradation)
client = NaiveOpenAI(api_key="your-api-key", degradation_rate=0.1)

# Example usage
completion = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "hello, how are you?"}
  ]
)

print(completion.choices[0].message)
```

## Configuration
- **API Key**: Your OpenAI API key.
- **Degradation Rate**: A float value between 0 and 1 representing the probability and impact of the API's performance degradation.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests with your new features and bug fixes.

## License
This project is licensed under the Apache-2.0 license - see the LICENSE file for details.

## Support
For support, raise issues directly in the GitHub repository or contact the maintainers through the project's homepage.

With this set up, developers can better prepare their applications to adapt under various performance conditions, enhancing both reliability and user experience.

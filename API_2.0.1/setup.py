from setuptools import setup, find_packages

setup(
    name='api-2.0.1',
    version='2.0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'requests>=2.0.0',
        'flask>=2.0.0',
        # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'api-2.0.1 = api_2.0.1.api.run_api_repl:main'
        ]
    },
)

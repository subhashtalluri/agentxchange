from setuptools import setup, find_packages

setup(
    name='agentxchange',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'websockets',
        'pydantic',
        'fastapi',
        'uvicorn',
        'httpx',
        'cryptography',
        'confluent-kafka',
        'tenacity',
        'typer[all]',
        'streamlit'
    ],
    entry_points={
        'console_scripts': [
            'agentx = cli.main:app'
        ]
    },
    author='Subhash Talluri',
    author_email='youremail@example.com',
    description='Modular agent communication framework with multi-transport support',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/subhashtalluri/agentxchange',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)

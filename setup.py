from setuptools import setup

setup(
    name="flask",
    version="2.2.0",
    description="Flask app template",
    author="Khoa",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["flask_singer_tap"],
    install_requires=[
        "singer-python==5.13.0",
        "requests==2.28.2",
        "flask==2.2.0",
        "flask_sqlalchemy",
        "jsonpickle"
        
    ],
    extras_require={
        "test": [
            "pylint==2.13.4",
            "nose"
        ],
        "dev": [
            "ipdb"
        ]
    },
    # entry_points="""
    # [console_scripts]
    # tap-tiktok-ads=tap_tiktok_ads:main
    # """,
    # packages=["tap_tiktok_ads"],
    # package_data = {
    #     "schemas": ["tap_tiktok_ads/schemas/*.json"]
    # },
    # include_package_data=True,
)
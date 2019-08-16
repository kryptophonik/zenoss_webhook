from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name="alerta-zenoss",
    version=version,
    description='Alerta Webhook for Zenoss',
    url='',
    license='',
    author='',
    author_email='',
    packages=find_packages(),
    py_modules=['alerta_zenoss'],
    install_requires=[''],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.webhooks': [
            'zenoss = alerta_zenoss:ZenossWebhook'
        ]
    }
)

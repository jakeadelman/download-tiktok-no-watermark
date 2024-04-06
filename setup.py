from setuptools import setup

setup(
    name='download_tiktok_no_watermark',
    version='0.2.0',    
    description='Download TikTok videos no watermark',
    url='https://github.com/jakeadelman/download_tiktok_no_watermark',
    author='Jacob Adelman',
    author_email='jacobzadelman@gmail.com',
    license='BSD 2-clause',
    packages=['download_tiktok_no_watermark'],
    install_requires=['beautifulsoup4==4.12.3'
                      ,'colorama==0.4.6',
                      'Requests==2.31.0',
                      'tls_client==1.0.1',
                      'js2py'                 
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
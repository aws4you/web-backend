# Installation

Before playing with the code you should create file /etc/default/env.LOCAL with the contents

    DJANGO_SECRET=$(python -c "print('A'*50)")
    DJANGO_DEBUG=True

Use your own value for the DJANGO_SECRET value

Configure uWSGI

    https://gist.github.com/willemarcel/a07917d21b7f3cce92da
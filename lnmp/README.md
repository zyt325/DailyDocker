sh init.sh

docker build -t harbor.base-fx.com/itd/php:7.3-fpm-mysql .

docker-compose up -d

更改php/www/wp-config.php，配置url和DB
```
define( 'DB_NAME', 'basefx' );

/** MySQL database username */
define( 'DB_USER', 'root' );

/** MySQL database password */
define( 'DB_PASSWORD', 'mysql325' );

/** MySQL hostname */
define( 'DB_HOST', 'db' );

define('WP_HOME','https://basemedia.base-fx.com');
define('WP_SITEURL','https://basemedia.base-fx.com');
/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

```
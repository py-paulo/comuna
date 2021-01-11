<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="profile" href="http://gmpg.org/xfn/11">
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <link href="https://fonts.googleapis.com" rel="preconnect" crossorigin="">
    <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin="">
    <title>Comuna - Home </title>
    <meta name="description" content="">
    <meta name="robots" content="noindex, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Comuna">
    <meta property="og:description" content="">
    <meta property="og:site_name" content="Comuna">
    <meta name="twitter:card" content="summary_large_image">
    <!-- / Yoast SEO plugin. -->
    <link rel="dns-prefetch" href="//fonts.googleapis.com">
    <link rel="dns-prefetch" href="//s.w.org">
    <style type="text/css">
        img.wp-smiley,
        img.emoji {
            display: inline !important;
            border: none !important;
            box-shadow: none !important;
            height: 1em !important;
            width: 1em !important;
            margin: 0 .07em !important;
            vertical-align: -0.1em !important;
            background: none !important;
            padding: 0 !important;
        }
    </style>
    <link rel="stylesheet" id="customify-font-stylesheet-0-css" href="https://fonts.googleapis.com/css2?family=Bungee:ital,wght@0,400&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Serif:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;family=IBM%20Plex%20Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;display=swap" type="text/css" media="all">
    <link rel="stylesheet" id="wp-block-library-css" href="assets/styles/css/style.min.css" type="text/css" media="all">
    <style id="wp-block-library-inline-css" type="text/css">
        .has-text-align-justify {
            text-align: justify;
        }
    </style>
    <link rel="stylesheet" id="wc-block-style-css" href="assets/styles/css/woocommerce-style.css" type="text/css" media="all">
    <link rel="stylesheet" id="woocommerce-layout-css" href="assets/styles/css/woocommerce-layout.css" type="text/css" media="all">
    <style id="woocommerce-layout-inline-css" type="text/css">
        .infinite-scroll .woocommerce-pagination {
            display: none;
        }
    </style>
    <link rel="stylesheet" id="woocommerce-smallscreen-css" href="assets/styles/css/woocommerce-smallscreen.css" type="text/css" media="only screen and (max-width: 768px)">
    <link rel="stylesheet" id="woocommerce-general-css" href="assets/styles/css/woocommerce.css" type="text/css" media="all">
    <style id="woocommerce-inline-inline-css" type="text/css">
        .woocommerce form .form-row .required {
            visibility: visible;
        }
    </style>
    <link rel="stylesheet" id="noto-google-fonts-css" href="//fonts.googleapis.com/css?family=Bungee%7CIBM+Plex+Sans%3A300%2C400%2C500%2C700&amp;subset=latin%2Clatin-ext&amp;ver=5.5.3" type="text/css" media="all">
    <link rel="stylesheet" id="noto-style-css" href="https://cdn.demos.pixelgrade.com/wp-content/themes/noto/style.css?ver=1608211413" type="text/css" media="all">
    <link rel="stylesheet" id="dashicons-css" href="https://demos.pixelgrade.com/noto/wp-includes/css/dashicons.min.css?ver=5.5.3" type="text/css" media="all">
    <link rel="stylesheet" id="zoom-instagram-widget-css" href="https://cdn.demos.pixelgrade.com/wp-content/plugins/instagram-widget-by-wpzoom/css/instagram-widget.css?ver=1608003618" type="text/css" media="all">
    <link rel="stylesheet" id="jetpack_css-css" href="https://cdn.demos.pixelgrade.com/wp-content/plugins/jetpack/css/jetpack.css?ver=1608003619" type="text/css" media="all">
    <!-- Custom Logo: hide header text -->
    <style id="custom-logo-css" type="text/css">
        .site-title {
            position: absolute;
            clip: rect(1px, 1px, 1px, 1px);
        }
    </style>
    <link rel="https://api.w.org/" href="https://demos.pixelgrade.com/noto/wp-json/">
    <link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://demos.pixelgrade.com/noto/xmlrpc.php?rsd">
    <link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://demos.pixelgrade.com/noto/wp-includes/wlwmanifest.xml">
    <link rel="shortlink" href="https://wp.me/9xCKi">
    <link rel="dns-prefetch" href="//v0.wordpress.com">
    <!-- Styles -->
    <link href="{{ asset('assets/styles/css/stylemain.css') }}" rel="stylesheet">
</head>

<body class="home blog wp-custom-logo theme-noto woocommerce-js site-title-hidden u-site-header-full-width u-underlined-links u-buttons-outline u-buttons-square u-content-background hfeed customify u-featured-images-animation u-pattern-waves">
    @include('home.partials._navbar')
    @include('home.partials._todo')
</body>

</html>
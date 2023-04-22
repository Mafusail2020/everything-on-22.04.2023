import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
headers2 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

song_name = input()
song_link = f'https://osu.ppy.sh/beatmapsets?q={song_name.replace(" ", "%20")}'
request = requests.get("https://osu.ppy.sh/beatmapsets", headers=headers2)


code = """<html prefix="og: http://ogp.me/ns#" lang="en" style="--vh:9.69px;"><head><style type="text/css">.turbolinks-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 9999;
  transition: width 300ms ease-out, opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}</style>
        





 















<link rel="stylesheet" media="all" href="/assets/css/app.494e19b4.css" data-turbolinks-track="reload">

<script>
    var currentLocale = "en";
    var fallbackLocale = "en";
</script>

<script src="/assets/js/runtime.bf0c1444.js" data-turbolinks-track="reload"></script>
<script src="/assets/js/vendor.27eaf413.js" data-turbolinks-track="reload"></script>


<script src="/assets/js/locales/en.474bd54d.js" data-turbolinks-track="reload"></script>

<script src="/assets/js/commons.7b1a5828.js" data-turbolinks-track="reload"></script>
<script src="/assets/js/app.82bc26e5.js" data-turbolinks-track="reload"></script>

<script src="/assets/js/moment-locales/en-gb.63f5394e.js" data-turbolinks-track="reload"></script>



        
    <link rel="apple-touch-icon" sizes="180x180" href="https://osu.ppy.sh/images/favicon/apple-touch-icon.png"><link rel="icon" sizes="32x32" href="https://osu.ppy.sh/images/favicon/favicon-32x32.png"><link rel="icon" sizes="16x16" href="https://osu.ppy.sh/images/favicon/favicon-16x16.png"><link rel="manifest" href="https://osu.ppy.sh/site.webmanifest"><link rel="mask-icon" href="https://osu.ppy.sh/images/favicon/safari-pinned-tab.svg" color="#e2609a"><meta name="msapplication-TileColor" content="#603cba"><meta name="theme-color" content="hsl(200, 10%, 40%)"><meta charset="utf-8"><meta name="description" content="Beatmaps Listing"><meta name="keywords" content="osu, peppy, ouendan, elite, beat, agents, ds, windows, game, taiko, tatsujin, simulator, sim, xna, ddr, beatmania, osu!, osume"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="csrf-param" content="_token"><meta name="csrf-token" content="UmOroUKsHiodxZ5qL206R3Fvhzl0G0Bo6viZl0ZO"><meta name="turbolinks-cache-control" content="no-preview"><title>beatmap listing | osu!</title></head>

    <body class="osu-layout osu-layout--body t-section action-index">
        <style>
            :root {
                --base-hue: 200;
                --base-hue-deg: 200deg;
            }
        </style>
        <div id="overlay" class="blackout blackout--overlay" style="display: none;"></div>
        <div class="blackout js-blackout" data-visibility="hidden"></div>

        
                    <div class="visible-xs no-print js-header--main">
    <div class="navbar-mobile-before"></div>

    <div class="navbar-mobile" role="navigation">
        <div class="navbar-mobile__header-section">
            <a class="navbar-mobile__logo" href="https://osu.ppy.sh/home"></a>
            <span class="navbar-mobile__brand u-ellipsis-overflow">
                beatmap listing
            </span>
        </div>

        <div class="navbar-mobile__header-section navbar-mobile__header-section--buttons">
            <button type="button" class="navbar-mobile__toggle js-click-menu" data-click-menu-target="mobile-menu">
                <span class="sr-only">Toggle navigation</span>
                <span class="navbar-mobile__toggle-icon">
                    <i class="fas fa-chevron-down"></i>
                </span>
            </button>
        </div>
    </div>

    <div class="mobile-menu js-click-menu u-fancy-scrollbar" data-click-menu-id="mobile-menu" data-visibility="hidden">
        <div class="mobile-menu__content">
            <div class="mobile-menu__tabs">
                                    <a href="https://osu.ppy.sh/users/21189675" data-click-menu-target="mobile-user" class="mobile-menu-tab mobile-menu-tab--user js-click-menu">
                        <span class="mobile-menu-tab__avatar">
                            <span class="avatar avatar--full-rounded" style="background-image: url('https://osu.ppy.sh/images/layout/avatar-guest.png');"></span>
                        </span>

                        <span class="u-ellipsis-overflow">
                            No_name_dot_com
                        </span>
                    </a>
                
                <button class="mobile-menu-tab js-click-menu" data-click-menu-target="mobile-nav">
                    <span class="fas fa-sitemap"></span>
                </button>

                                    <button class="mobile-menu-tab js-click-menu" data-click-menu-target="mobile-search">
                        <span class="fas fa-search"></span>
                    </button>

                    <a class="mobile-menu-tab js-click-menu js-react--chat-icon" data-click-menu-target="mobile-chat-notification" data-turbolinks-permanent="" data-type="mobile" id="notification-widget-chat-icon-mobile" href="https://osu.ppy.sh/community/chat"><span class="notification-icon notification-icon--mobile"><i class="fas fa-comment-alt"></i><span class="notification-icon__count">0</span></span></a>

                    <a class="mobile-menu-tab js-click-menu js-react--main-notification-icon" data-click-menu-target="mobile-notification" data-turbolinks-permanent="" data-type="mobile" id="notification-widget-icon-mobile" href="https://osu.ppy.sh/notifications"><span class="notification-icon notification-icon--mobile"><i class="fas fa-inbox"></i><span class="notification-icon__count">0</span></span></a>
                            </div>

            <div class="mobile-menu__item js-click-menu" data-click-menu-id="mobile-user" data-visibility="hidden">
                <div class="navbar-mobile-item js-click-menu--close">
            <div class="navbar-mobile-item__main js-react--user-card" data-is-current-user="1"><div class="user-card user-card--highlightable user-card--card"><a class="user-card__background-container" href="https://osu.ppy.sh/users/21189675"><img class="user-card__background" src="https://osu.ppy.sh/images/headers/profile-covers/c4.jpg"><div class="user-card__background-overlay user-card__background-overlay--online"></div></a><div class="user-card__card"><div class="user-card__content user-card__content--details"><div class="user-card__user"><div class="user-card__avatar-space"><div class="user-card__avatar-spinner user-card__avatar-spinner--loaded"><div class="la-ball-clip-rotate la-ball-clip-rotate--loaded"></div></div><img class="user-card__avatar user-card__avatar--loaded" src="https://osu.ppy.sh/images/layout/avatar-guest.png"></div></div><div class="user-card__details"><div class="user-card__icons user-card__icons--card"><a class="user-card__icon user-card__icon--flag" href="https://osu.ppy.sh/rankings/osu/performance?country=UA"><div class="flag-country" title="Ukraine" style="background-image: url(&quot;/assets/images/flags/1f1fa-1f1e6.svg&quot;);"></div></a><div class="user-card__icon"></div><div class="user-card__icon"></div></div><div class="user-card__username-row"><a class="user-card__username u-ellipsis-pre-overflow" href="https://osu.ppy.sh/users/21189675">No_name_dot_com</a><div class="user-card__group-badges"></div></div></div></div><div class="user-card__content user-card__content--status"><div class="user-card__status"><div class="user-card__status-icon-container"><div class="user-card__status-icon user-card__status-icon--online"></div></div><div class="user-card__status-messages"><span class="user-card__status-message user-card__status-message--sub u-ellipsis-overflow"></span><span class="user-card__status-message u-ellipsis-overflow">Online</span></div></div><div class="user-card__icons user-card__icons--menu"></div></div></div></div></div>

        <a class="navbar-mobile-item__main" href="https://osu.ppy.sh/users/21189675">
            My Profile
        </a>

        <a class="navbar-mobile-item__main" href="https://osu.ppy.sh/home/friends">
            Friends
        </a>

        <a class="navbar-mobile-item__main" href="https://osu.ppy.sh/home/follows/forum_topic">
            Watchlists
        </a>

        <a class="navbar-mobile-item__main" href="https://osu.ppy.sh/home/account/edit">
            Settings
        </a>

        <button class="js-logout-link navbar-mobile-item__main" type="button" data-url="https://osu.ppy.sh/session" data-confirm="Are you sure you want to sign out? :(" data-method="delete" data-remote="1">
            Sign Out
        </button>
    </div>
            </div>

            <div class="mobile-menu__item js-click-menu" data-click-menu-id="mobile-nav" data-visibility="hidden">
                <div class="navbar-mobile-item">
        <a data-click-menu-target="nav-mobile-home" class="navbar-mobile-item__main js-click-menu" href="https://osu.ppy.sh/home">
            <span class="navbar-mobile-item__icon navbar-mobile-item__icon--closed">
                <i class="fas fa-chevron-right"></i>
            </span>

            <span class="navbar-mobile-item__icon navbar-mobile-item__icon--opened">
                <i class="fas fa-chevron-down"></i>
            </span>

            home
        </a>

        <ul class="navbar-mobile-item__submenu js-click-menu" data-click-menu-id="nav-mobile-home" data-visibility="hidden">
                                                                                <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/news">
                        news
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/wiki/en/Team">
                        team
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/changelog">
                        changelog
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/download">
                        download
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/search">
                        search
                    </a>
                </li>
                    </ul>
    </div>
    <div class="navbar-mobile-item">
        <a data-click-menu-target="nav-mobile-beatmaps" class="navbar-mobile-item__main js-click-menu" href="https://osu.ppy.sh/beatmapsets">
            <span class="navbar-mobile-item__icon navbar-mobile-item__icon--closed">
                <i class="fas fa-chevron-right"></i>
            </span>

            <span class="navbar-mobile-item__icon navbar-mobile-item__icon--opened">
                <i class="fas fa-chevron-down"></i>
            </span>

            beatmaps
        </a>

        <ul class="navbar-mobile-item__submenu js-click-menu" data-click-menu-id="nav-mobile-beatmaps" data-visibility="hidden">
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/beatmapsets">
                        beatmap listing
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/beatmaps/artists">
                        featured artists
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/beatmaps/packs">
                        beatmap packs
                    </a>
                </li>
                    </ul>
    </div>
    <div class="navbar-mobile-item">
        <a data-click-menu-target="nav-mobile-rankings" class="navbar-mobile-item__main js-click-menu" href="https://osu.ppy.sh/rankings/osu/performance">
            <span class="navbar-mobile-item__icon navbar-mobile-item__icon--closed">
                <i class="fas fa-chevron-right"></i>
            </span>

            <span class="navbar-mobile-item__icon navbar-mobile-item__icon--opened">
                <i class="fas fa-chevron-down"></i>
            </span>

            rankings
        </a>

        <ul class="navbar-mobile-item__submenu js-click-menu" data-click-menu-id="nav-mobile-rankings" data-visibility="hidden">
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/rankings/osu/performance">
                        performance
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/rankings/osu/charts">
                        spotlights
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/rankings/osu/score">
                        score
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/rankings/osu/country">
                        country
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/multiplayer/rooms/latest">
                        multiplayer
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/p/kudosu">
                        kudosu
                    </a>
                </li>
                    </ul>
    </div>
    <div class="navbar-mobile-item">
        <a data-click-menu-target="nav-mobile-community" class="navbar-mobile-item__main js-click-menu" href="https://osu.ppy.sh/community/forums">
            <span class="navbar-mobile-item__icon navbar-mobile-item__icon--closed">
                <i class="fas fa-chevron-right"></i>
            </span>

            <span class="navbar-mobile-item__icon navbar-mobile-item__icon--opened">
                <i class="fas fa-chevron-down"></i>
            </span>

            community
        </a>

        <ul class="navbar-mobile-item__submenu js-click-menu" data-click-menu-id="nav-mobile-community" data-visibility="hidden">
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/community/forums">
                        forum
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/community/chat">
                        chat
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/community/contests">
                        contests
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/community/tournaments">
                        tournaments
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/community/livestreams">
                        live streams
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://discord.gg/ppy">
                        development
                    </a>
                </li>
                    </ul>
    </div>
    <div class="navbar-mobile-item">
        <a data-click-menu-target="nav-mobile-store" class="navbar-mobile-item__main js-click-menu" href="https://osu.ppy.sh/store/listing">
            <span class="navbar-mobile-item__icon navbar-mobile-item__icon--closed">
                <i class="fas fa-chevron-right"></i>
            </span>

            <span class="navbar-mobile-item__icon navbar-mobile-item__icon--opened">
                <i class="fas fa-chevron-down"></i>
            </span>

            store
        </a>

        <ul class="navbar-mobile-item__submenu js-click-menu" data-click-menu-id="nav-mobile-store" data-visibility="hidden">
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/store/listing">
                        products
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/store/cart">
                        cart
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/store/orders">
                        order history
                    </a>
                </li>
                    </ul>
    </div>
    <div class="navbar-mobile-item">
        <a data-click-menu-target="nav-mobile-help" class="navbar-mobile-item__main js-click-menu" href="https://osu.ppy.sh/wiki/en/Main_Page">
            <span class="navbar-mobile-item__icon navbar-mobile-item__icon--closed">
                <i class="fas fa-chevron-right"></i>
            </span>

            <span class="navbar-mobile-item__icon navbar-mobile-item__icon--opened">
                <i class="fas fa-chevron-down"></i>
            </span>

            help
        </a>

        <ul class="navbar-mobile-item__submenu js-click-menu" data-click-menu-id="nav-mobile-help" data-visibility="hidden">
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/wiki/en/Main_Page">
                        wiki
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/wiki/en/FAQ">
                        faq
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/wiki/en/Rules">
                        rules
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/wiki/en/Reporting_Bad_Behaviour/Abuse">
                        report abuse
                    </a>
                </li>
                                            <li>
                    <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/wiki/en/Help_Centre">
                        no, really, i need help!
                    </a>
                </li>
                    </ul>
    </div>

<div class="navbar-mobile-item">
    <button class="navbar-mobile-item__main js-click-menu" data-click-menu-target="nav-mobile-locale">
        <span class="navbar-mobile-item__icon navbar-mobile-item__icon--closed">
            <i class="fas fa-chevron-right"></i>
        </span>

        <span class="navbar-mobile-item__icon navbar-mobile-item__icon--opened">
            <i class="fas fa-chevron-down"></i>
        </span>

        <span class="navbar-mobile-item__locale-flag">
            <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1ec-1f1e7.svg');"></div>
        </span>

        English
    </button>

    <ul class="navbar-mobile-item__submenu js-click-menu" data-click-menu-id="nav-mobile-locale" data-visibility="hidden">
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=en" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1ec-1f1e7.svg');"></div>
                    </span>

                    English
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=ar" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1f8-1f1e6.svg');"></div>
                    </span>

                    اَلْعَرَبِيَّةُ‎
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=be" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1e7-1f1fe.svg');"></div>
                    </span>

                    Беларуская мова
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=bg" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1e7-1f1ec.svg');"></div>
                    </span>

                    Български
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=cs" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1e8-1f1ff.svg');"></div>
                    </span>

                    Česky
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=da" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1e9-1f1f0.svg');"></div>
                    </span>

                    Dansk
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=de" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1e9-1f1ea.svg');"></div>
                    </span>

                    Deutsch
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=el" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1ec-1f1f7.svg');"></div>
                    </span>

                    Ελληνικά
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=es" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1ea-1f1f8.svg');"></div>
                    </span>

                    español
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=fi" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1eb-1f1ee.svg');"></div>
                    </span>

                    Suomi
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=fr" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1eb-1f1f7.svg');"></div>
                    </span>

                    français
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=hu" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1ed-1f1fa.svg');"></div>
                    </span>

                    Magyar
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=id" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1ee-1f1e9.svg');"></div>
                    </span>

                    Bahasa Indonesia
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=it" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1ee-1f1f9.svg');"></div>
                    </span>

                    Italiano
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=ja" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1ef-1f1f5.svg');"></div>
                    </span>

                    日本語
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=ko" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1f0-1f1f7.svg');"></div>
                    </span>

                    한국어
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=nl" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1f3-1f1f1.svg');"></div>
                    </span>

                    Nederlands
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=no" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1f3-1f1f4.svg');"></div>
                    </span>

                    Norsk
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=pl" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1f5-1f1f1.svg');"></div>
                    </span>

                    polski
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=pt" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1f5-1f1f9.svg');"></div>
                    </span>

                    Português
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=pt-br" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1e7-1f1f7.svg');"></div>
                    </span>

                    Português (Brasil)
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=ro" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1f7-1f1f4.svg');"></div>
                    </span>

                    Română
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=ru" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1f7-1f1fa.svg');"></div>
                    </span>

                    Русский
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=sk" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1f8-1f1f0.svg');"></div>
                    </span>

                    Slovenčina
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=sv" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1f8-1f1ea.svg');"></div>
                    </span>

                    Svenska
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=th" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1f9-1f1ed.svg');"></div>
                    </span>

                    ไทย
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=tr" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1f9-1f1f7.svg');"></div>
                    </span>

                    Türkçe
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=uk" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1fa-1f1e6.svg');"></div>
                    </span>

                    Українська мова
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=vi" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1fb-1f1f3.svg');"></div>
                    </span>

                    Tiếng Việt
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=zh" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1e8-1f1f3.svg');"></div>
                    </span>

                    简体中文
                </a>
            </li>
                                <li>
                <a class="navbar-mobile-item__submenu-item js-click-menu--close" href="https://osu.ppy.sh/home/set-locale?locale=zh-tw" data-remote="1" data-method="POST">
                    <span class="navbar-mobile-item__locale-flag">
                        <div class="flag-country flag-country--small flag-country--flat" style="background-image: url('/assets/images/flags/1f1f9-1f1fc.svg');"></div>
                    </span>

                    繁體中文（台灣）
                </a>
            </li>
            </ul>
</div>
            </div>

                            <div class="mobile-menu__item mobile-menu__item--search js-click-menu js-react--quick-search" data-click-menu-id="mobile-search" data-visibility="hidden"><div class="quick-search u-fancy-scrollbar"><div class="quick-search-input"><div class="quick-search-input__field"><span class="quick-search-input__icon"><span class="fas fa-search"></span></span><input class="quick-search-input__input js-click-menu--autofocus" placeholder="type to search" value=""></div></div></div></div>

                <div class="mobile-menu__item js-click-menu js-react--notification-widget" data-click-menu-id="mobile-chat-notification" data-notification-widget="{&quot;only&quot;:&quot;channel&quot;}" data-visibility="hidden" data-turbolinks-permanent="" id="notification-widget-chat-mobile"><div class="notification-popup u-fancy-scrollbar "><div class="notification-popup__scroll-container"><div class="notification-popup__buttons"><a class="notification-popup__filter" href="https://osu.ppy.sh/community/chat">go to chat</a><div class="notification-popup__clear-button"></div></div><div class="notification-stacks"><p class="notification-popup__empty">No notifications</p></div></div></div></div>

                <div class="mobile-menu__item js-click-menu js-react--notification-widget" data-click-menu-id="mobile-notification" data-notification-widget="{&quot;excludes&quot;:[&quot;channel&quot;]}" data-visibility="hidden" data-turbolinks-permanent="" id="notification-widget-mobile"><div class="notification-popup u-fancy-scrollbar "><div class="notification-popup__scroll-container"><div class="notification-popup__filters"><button class="notification-popup__filter notification-popup__filter--active"><span class="notification-popup__filter-count">0</span><span>all</span></button></div><div class="notification-popup__buttons"><a class="notification-popup__filter" href="https://osu.ppy.sh/notifications">see all notifications</a><div class="notification-popup__clear-button"></div></div><div class="notification-stacks"><p class="notification-popup__empty">All notifications read!</p></div></div></div></div>
                    </div>
    </div>
</div>

<div class="
    js-pinned-header
    hidden-xs
    no-print
    nav2-header
">
    <div class="nav2-header__body">
        <div class="nav2-header__menu-bg js-nav2--menu-bg" data-visibility="hidden"></div>
        <div class="nav2-header__triangles"></div>
        <div class="nav2-header__transition-overlay"></div>

        <div class="osu-page">
            <div class="nav2 js-nav-button">
    <div class="nav2__colgroup nav2__colgroup--menu js-nav-button--container">
        <div class="nav2__col nav2__col--logo">
            <a href="https://osu.ppy.sh/home" class="nav2__logo-link">
                <div class="nav2__logo nav2__logo--bg"></div>
                <div class="nav2__logo"></div>
            </a>
        </div>

                    <div class="nav2__col nav2__col--menu">
                <a class="nav2__menu-link-main js-menu" href="https://osu.ppy.sh/home" data-menu-target="nav2-menu-popup-home" data-menu-show-delay="0">
                    <span class="u-relative">
                        home

                                            </span>
                </a>

                <div class="nav2__menu-popup">
                    <div class="
                            simple-menu
                            simple-menu--nav2
                            simple-menu--nav2-left-aligned
                            simple-menu--nav2-transparent
                            js-menu
                        " data-menu-id="nav2-menu-popup-home" data-visibility="hidden">
                                                                                                                                            <a class="simple-menu__item u-section-home--before-bg-normal" href="https://osu.ppy.sh/home/news">
                                news
                            </a>
                                                                                <a class="simple-menu__item u-section-home--before-bg-normal" href="https://osu.ppy.sh/wiki/en/Team">
                                team
                            </a>
                                                                                <a class="simple-menu__item u-section-home--before-bg-normal" href="https://osu.ppy.sh/home/changelog">
                                changelog
                            </a>
                                                                                <a class="simple-menu__item u-section-home--before-bg-normal" href="https://osu.ppy.sh/home/download">
                                download
                            </a>
                                                                                <a class="simple-menu__item u-section-home--before-bg-normal" href="https://osu.ppy.sh/home/search">
                                search
                            </a>
                                            </div>
                </div>
            </div>
                    <div class="nav2__col nav2__col--menu">
                <a class="nav2__menu-link-main js-menu" href="https://osu.ppy.sh/beatmapsets" data-menu-target="nav2-menu-popup-beatmaps" data-menu-show-delay="0">
                    <span class="u-relative">
                        beatmaps

                                                    <span class="nav2__menu-link-bar u-section--bg-normal"></span>
                                            </span>
                </a>

                <div class="nav2__menu-popup">
                    <div class="
                            simple-menu
                            simple-menu--nav2
                            simple-menu--nav2-left-aligned
                            simple-menu--nav2-transparent
                            js-menu
                        " data-menu-id="nav2-menu-popup-beatmaps" data-visibility="hidden">
                                                                                <a class="simple-menu__item u-section-beatmaps--before-bg-normal" href="https://osu.ppy.sh/beatmapsets">
                                beatmap listing
                            </a>
                                                                                <a class="simple-menu__item u-section-beatmaps--before-bg-normal" href="https://osu.ppy.sh/beatmaps/artists">
                                featured artists
                            </a>
                                                                                <a class="simple-menu__item u-section-beatmaps--before-bg-normal" href="https://osu.ppy.sh/beatmaps/packs">
                                beatmap packs
                            </a>
                                            </div>
                </div>
            </div>
                    <div class="nav2__col nav2__col--menu">
                <a class="nav2__menu-link-main js-menu" href="https://osu.ppy.sh/rankings/osu/performance" data-menu-target="nav2-menu-popup-rankings" data-menu-show-delay="0">
                    <span class="u-relative">
                        rankings

                                            </span>
                </a>

                <div class="nav2__menu-popup">
                    <div class="
                            simple-menu
                            simple-menu--nav2
                            simple-menu--nav2-left-aligned
                            simple-menu--nav2-transparent
                            js-menu
                        " data-menu-id="nav2-menu-popup-rankings" data-visibility="hidden">
                                                                                <a class="simple-menu__item u-section-rankings--before-bg-normal" href="https://osu.ppy.sh/rankings/osu/performance">
                                performance
                            </a>
                                                                                <a class="simple-menu__item u-section-rankings--before-bg-normal" href="https://osu.ppy.sh/rankings/osu/charts">
                                spotlights
                            </a>
                                                                                <a class="simple-menu__item u-section-rankings--before-bg-normal" href="https://osu.ppy.sh/rankings/osu/score">
                                score
                            </a>
                                                                                <a class="simple-menu__item u-section-rankings--before-bg-normal" href="https://osu.ppy.sh/rankings/osu/country">
                                country
                            </a>
                                                                                <a class="simple-menu__item u-section-rankings--before-bg-normal" href="https://osu.ppy.sh/multiplayer/rooms/latest">
                                multiplayer
                            </a>
                                                                                <a class="simple-menu__item u-section-rankings--before-bg-normal" href="https://osu.ppy.sh/p/kudosu">
                                kudosu
                            </a>
                                            </div>
                </div>
            </div>
                    <div class="nav2__col nav2__col--menu">
                <a class="nav2__menu-link-main js-menu" href="https://osu.ppy.sh/community/forums" data-menu-target="nav2-menu-popup-community" data-menu-show-delay="0">
                    <span class="u-relative">
                        community

                                            </span>
                </a>

                <div class="nav2__menu-popup">
                    <div class="
                            simple-menu
                            simple-menu--nav2
                            simple-menu--nav2-left-aligned
                            simple-menu--nav2-transparent
                            js-menu
                        " data-menu-id="nav2-menu-popup-community" data-visibility="hidden">
                                                                                <a class="simple-menu__item u-section-community--before-bg-normal" href="https://osu.ppy.sh/community/forums">
                                forum
                            </a>
                                                                                <a class="simple-menu__item u-section-community--before-bg-normal" href="https://osu.ppy.sh/community/chat">
                                chat
                            </a>
                                                                                <a class="simple-menu__item u-section-community--before-bg-normal" href="https://osu.ppy.sh/community/contests">
                                contests
                            </a>
                                                                                <a class="simple-menu__item u-section-community--before-bg-normal" href="https://osu.ppy.sh/community/tournaments">
                                tournaments
                            </a>
                                                                                <a class="simple-menu__item u-section-community--before-bg-normal" href="https://osu.ppy.sh/community/livestreams">
                                live streams
                            </a>
                                                                                <a class="simple-menu__item u-section-community--before-bg-normal" href="https://discord.gg/ppy">
                                development
                            </a>
                                            </div>
                </div>
            </div>
                    <div class="nav2__col nav2__col--menu">
                <a class="nav2__menu-link-main js-menu" href="https://osu.ppy.sh/store/listing" data-menu-target="nav2-menu-popup-store" data-menu-show-delay="0">
                    <span class="u-relative">
                        store

                                            </span>
                </a>

                <div class="nav2__menu-popup">
                    <div class="
                            simple-menu
                            simple-menu--nav2
                            simple-menu--nav2-left-aligned
                            simple-menu--nav2-transparent
                            js-menu
                        " data-menu-id="nav2-menu-popup-store" data-visibility="hidden">
                                                                                <a class="simple-menu__item u-section-store--before-bg-normal" href="https://osu.ppy.sh/store/listing">
                                products
                            </a>
                                                                                <a class="simple-menu__item u-section-store--before-bg-normal" href="https://osu.ppy.sh/store/cart">
                                cart
                            </a>
                                                                                <a class="simple-menu__item u-section-store--before-bg-normal" href="https://osu.ppy.sh/store/orders">
                                order history
                            </a>
                                            </div>
                </div>
            </div>
                    <div class="nav2__col nav2__col--menu">
                <a class="nav2__menu-link-main js-menu" href="https://osu.ppy.sh/wiki/en/Main_Page" data-menu-target="nav2-menu-popup-help" data-menu-show-delay="0">
                    <span class="u-relative">
                        help

                                            </span>
                </a>

                <div class="nav2__menu-popup">
                    <div class="
                            simple-menu
                            simple-menu--nav2
                            simple-menu--nav2-left-aligned
                            simple-menu--nav2-transparent
                            js-menu
                        " data-menu-id="nav2-menu-popup-help" data-visibility="hidden">
                                                                                <a class="simple-menu__item u-section-help--before-bg-normal" href="https://osu.ppy.sh/wiki/en/Main_Page">
                                wiki
                            </a>
                                                                                <a class="simple-menu__item u-section-help--before-bg-normal" href="https://osu.ppy.sh/wiki/en/FAQ">
                                faq
                            </a>
                                                                                <a class="simple-menu__item u-section-help--before-bg-normal" href="https://osu.ppy.sh/wiki/en/Rules">
                                rules
                            </a>
                                                                                <a class="simple-menu__item u-section-help--before-bg-normal" href="https://osu.ppy.sh/wiki/en/Reporting_Bad_Behaviour/Abuse">
                                report abuse
                            </a>
                                                                                <a class="simple-menu__item u-section-help--before-bg-normal" href="https://osu.ppy.sh/wiki/en/Help_Centre">
                                no, really, i need help!
                            </a>
                                            </div>
                </div>
            </div>
        
        <div class="nav2__col nav2__col--menu js-react--quick-search-button"><a class="nav2__menu-link-main nav2__menu-link-main--search" href="https://osu.ppy.sh/home/search"><span class="fas fa-search"></span></a></div>
    </div>
    <div class="nav2__colgroup js-nav-button--container">
        <div class="nav2__col js-nav-button--item">
            <a href="https://osu.ppy.sh/wiki/Twitter" class="nav-button nav-button--social" data-orig-title="Twitter" data-hasqtip="93">
                <span class="fab fa-twitter"></span>
            </a>
        </div>

        <div class="nav2__col">
            <a href="https://osu.ppy.sh/home/support" class="nav-button nav-button--support" title="support the game">
                <span class="fas fa-heart"></span>
            </a>
        </div>

        <div class="nav2__col">
            <button class="nav-button nav-button--stadium js-click-menu" data-click-menu-target="nav2-locale-popup">
                <span class="nav-button__locale-current-flag">
                    <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1ec-1f1e7.svg');"></div>
                </span>
            </button>

            <div class="nav-click-popup">
                <div class="simple-menu simple-menu--nav2 simple-menu--nav2-locales js-click-menu js-nav2--centered-popup hidden" data-click-menu-id="nav2-locale-popup" data-visibility="hidden">
                    <div class="simple-menu__content">
                                                                                <button type="button" class="
                                    simple-menu__item
                                    simple-menu__item--active
                                ">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1ec-1f1e7.svg');"></div>
                                    </span>

                                    English
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=ar" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1f8-1f1e6.svg');"></div>
                                    </span>

                                    اَلْعَرَبِيَّةُ‎
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=be" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1e7-1f1fe.svg');"></div>
                                    </span>

                                    Беларуская мова
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=bg" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1e7-1f1ec.svg');"></div>
                                    </span>

                                    Български
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=cs" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1e8-1f1ff.svg');"></div>
                                    </span>

                                    Česky
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=da" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1e9-1f1f0.svg');"></div>
                                    </span>

                                    Dansk
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=de" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1e9-1f1ea.svg');"></div>
                                    </span>

                                    Deutsch
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=el" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1ec-1f1f7.svg');"></div>
                                    </span>

                                    Ελληνικά
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=es" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1ea-1f1f8.svg');"></div>
                                    </span>

                                    español
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=fi" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1eb-1f1ee.svg');"></div>
                                    </span>

                                    Suomi
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=fr" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1eb-1f1f7.svg');"></div>
                                    </span>

                                    français
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=hu" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1ed-1f1fa.svg');"></div>
                                    </span>

                                    Magyar
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=id" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1ee-1f1e9.svg');"></div>
                                    </span>

                                    Bahasa Indonesia
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=it" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1ee-1f1f9.svg');"></div>
                                    </span>

                                    Italiano
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=ja" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1ef-1f1f5.svg');"></div>
                                    </span>

                                    日本語
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=ko" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1f0-1f1f7.svg');"></div>
                                    </span>

                                    한국어
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=nl" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1f3-1f1f1.svg');"></div>
                                    </span>

                                    Nederlands
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=no" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1f3-1f1f4.svg');"></div>
                                    </span>

                                    Norsk
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=pl" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1f5-1f1f1.svg');"></div>
                                    </span>

                                    polski
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=pt" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1f5-1f1f9.svg');"></div>
                                    </span>

                                    Português
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=pt-br" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1e7-1f1f7.svg');"></div>
                                    </span>

                                    Português (Brasil)
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=ro" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1f7-1f1f4.svg');"></div>
                                    </span>

                                    Română
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=ru" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1f7-1f1fa.svg');"></div>
                                    </span>

                                    Русский
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=sk" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1f8-1f1f0.svg');"></div>
                                    </span>

                                    Slovenčina
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=sv" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1f8-1f1ea.svg');"></div>
                                    </span>

                                    Svenska
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=th" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1f9-1f1ed.svg');"></div>
                                    </span>

                                    ไทย
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=tr" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1f9-1f1f7.svg');"></div>
                                    </span>

                                    Türkçe
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=uk" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1fa-1f1e6.svg');"></div>
                                    </span>

                                    Українська мова
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=vi" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1fb-1f1f3.svg');"></div>
                                    </span>

                                    Tiếng Việt
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=zh" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1e8-1f1f3.svg');"></div>
                                    </span>

                                    简体中文
                                </span>
                            </button>
                                                                                <button type="button" class="
                                    simple-menu__item
                                    
                                " data-url="https://osu.ppy.sh/home/set-locale?locale=zh-tw" data-remote="1" data-method="POST">
                                <span class="nav2-locale-item">
                                    <span class="nav2-locale-item__flag">
                                        <div class="flag-country flag-country--flat" style="background-image: url('/assets/images/flags/1f1f9-1f1fc.svg');"></div>
                                    </span>

                                    繁體中文（台灣）
                                </span>
                            </button>
                                            </div>
                </div>
            </div>
        </div>

                    <div class="nav2__col">
                <a class="nav-button nav-button--stadium js-click-menu js-react--chat-icon" data-click-menu-target="nav2-chat-notification-widget" data-turbolinks-permanent="" id="notification-widget-chat-icon" href="https://osu.ppy.sh/community/chat"><span class="notification-icon"><i class="fas fa-comment-alt"></i><span class="notification-icon__count">0</span></span></a>
                <div class="nav-click-popup js-click-menu js-react--notification-widget" data-click-menu-id="nav2-chat-notification-widget" data-visibility="hidden" data-notification-widget="{&quot;extraClasses&quot;:&quot;js-nav2--centered-popup hidden&quot;,&quot;only&quot;:&quot;channel&quot;}" data-turbolinks-permanent="" id="notification-widget-chat"><div class="notification-popup u-fancy-scrollbar js-nav2--centered-popup hidden"><div class="notification-popup__scroll-container"><div class="notification-popup__buttons"><a class="notification-popup__filter" href="https://osu.ppy.sh/community/chat">go to chat</a><div class="notification-popup__clear-button"></div></div><div class="notification-stacks"><p class="notification-popup__empty">No notifications</p></div></div></div></div>

            </div>

            <div class="nav2__col">
                <a class="nav-button nav-button--stadium js-click-menu js-react--main-notification-icon" data-click-menu-target="nav2-notification-widget" data-turbolinks-permanent="" id="notification-widget-icon" href="https://osu.ppy.sh/notifications"><span class="notification-icon"><i class="fas fa-inbox"></i><span class="notification-icon__count">0</span></span></a>
                <div class="nav-click-popup js-click-menu js-react--notification-widget" data-click-menu-id="nav2-notification-widget" data-visibility="hidden" data-notification-widget="{&quot;extraClasses&quot;:&quot;js-nav2--centered-popup hidden&quot;,&quot;excludes&quot;:[&quot;channel&quot;]}" data-turbolinks-permanent="" id="notification-widget"><div class="notification-popup u-fancy-scrollbar js-nav2--centered-popup hidden"><div class="notification-popup__scroll-container"><div class="notification-popup__filters"><button class="notification-popup__filter notification-popup__filter--active"><span class="notification-popup__filter-count">0</span><span>all</span></button></div><div class="notification-popup__buttons"><a class="notification-popup__filter" href="https://osu.ppy.sh/notifications">see all notifications</a><div class="notification-popup__clear-button"></div></div><div class="notification-stacks"><p class="notification-popup__empty">All notifications read!</p></div></div></div></div>
            </div>
        
        <div class="nav2__col nav2__col--avatar">
            <a class="avatar avatar--nav2 js-current-user-avatar js-click-menu js-user-login--menu js-user-header" data-click-menu-target="nav2-user-popup" href="https://osu.ppy.sh/users/21189675" style="background-image:url('https://osu.ppy.sh/images/layout/avatar-guest.png');"></a>

            <div class="nav-click-popup nav-click-popup--user js-user-header-popup">
                                    <div class="simple-menu simple-menu--nav2 js-click-menu js-nav2--centered-popup hidden" data-click-menu-id="nav2-user-popup" data-visibility="hidden">
    <a href="https://osu.ppy.sh/users/21189675" class="simple-menu__header simple-menu__header--link js-current-user-cover" style="background-image:url('https://osu.ppy.sh/images/headers/profile-covers/c4.jpg');">
        <img class="simple-menu__header-icon" src="/images/icons/profile.svg" alt="">
        <div class="u-relative">No_name_dot_com</div>
    </a>

    <a class="simple-menu__item" href="https://osu.ppy.sh/users/21189675">
        My Profile
    </a>

    <a class="simple-menu__item" href="https://osu.ppy.sh/home/friends">
        Friends
    </a>

    <a class="simple-menu__item" href="https://osu.ppy.sh/home/follows/forum_topic">
        Watchlists
    </a>

    <a class="simple-menu__item" href="https://osu.ppy.sh/home/account/edit">
        Settings
    </a>

    <button class="js-logout-link simple-menu__item" type="button" data-url="https://osu.ppy.sh/session" data-confirm="Are you sure you want to sign out? :(" data-method="delete" data-remote="1">
        Sign Out
    </button>
</div>
                            </div>
        </div>
    </div>
</div>
        </div>
    </div>
    <div class="js-pinned-header-sticky sticky-header js-sync-height--reference" data-sync-height-target="sticky-header" data-visibility="hidden" data-visibility-animation="none">
    <div class="osu-page">
        
        
                    <div class="sticky-header__body">
                <div class="js-sticky-header-breadcrumbs sticky-header__breadcrumbs">
                                        <div id="search-panel-breadcrumbs-portal"><ol class="sticky-header-breadcrumbs"><li class="sticky-header-breadcrumbs__item"><span class="sticky-header-breadcrumbs__link">Beatmaps</span></li><li class="sticky-header-breadcrumbs__item"><span class="sticky-header-breadcrumbs__link">search</span></li></ol></div></div>
                <div class="js-sticky-header-content sticky-header__content">
                                        <div id="search-panel-content-portal"><div class="beatmapsets-search beatmapsets-search--sticky"><div class="beatmapsets-search__input-container"><input class="beatmapsets-search__input js-beatmapsets-search-input" name="search" placeholder="type in keywords..." value=""><div class="beatmapsets-search__icon"><i class="fas fa-search"></i></div></div><div class="beatmapsets-search__filters"><div class="beatmapsets-search-filter"><div class="beatmapsets-search-filter__items"><a class="beatmapsets-search-filter__item" data-filter-value="any" href="https://osu.ppy.sh/beatmapsets?s=any">Any</a><a class="beatmapsets-search-filter__item beatmapsets-search-filter__item--active" data-filter-value="leaderboard" href="https://osu.ppy.sh/beatmapsets">Has Leaderboard</a><a class="beatmapsets-search-filter__item" data-filter-value="ranked" href="https://osu.ppy.sh/beatmapsets?s=ranked">Ranked</a><a class="beatmapsets-search-filter__item" data-filter-value="qualified" href="https://osu.ppy.sh/beatmapsets?s=qualified">Qualified</a><a class="beatmapsets-search-filter__item" data-filter-value="loved" href="https://osu.ppy.sh/beatmapsets?s=loved">Loved</a><a class="beatmapsets-search-filter__item" data-filter-value="favourites" href="https://osu.ppy.sh/beatmapsets?s=favourites">Favourites</a><a class="beatmapsets-search-filter__item" data-filter-value="pending" href="https://osu.ppy.sh/beatmapsets?s=pending">Pending</a><a class="beatmapsets-search-filter__item" data-filter-value="wip" href="https://osu.ppy.sh/beatmapsets?s=wip">WIP</a><a class="beatmapsets-search-filter__item" data-filter-value="graveyard" href="https://osu.ppy.sh/beatmapsets?s=graveyard">Graveyard</a><a class="beatmapsets-search-filter__item" data-filter-value="mine" href="https://osu.ppy.sh/beatmapsets?s=mine">My Maps</a></div></div><div class="beatmapsets-search-filter"><div class="beatmapsets-search-filter__items"><a class="beatmapsets-search-filter__item beatmapsets-search-filter__item--active" href="https://osu.ppy.sh/beatmapsets">Any</a><a class="beatmapsets-search-filter__item" data-filter-value="0" href="https://osu.ppy.sh/beatmapsets?m=0">osu!</a><a class="beatmapsets-search-filter__item" data-filter-value="1" href="https://osu.ppy.sh/beatmapsets?m=1">osu!taiko</a><a class="beatmapsets-search-filter__item" data-filter-value="2" href="https://osu.ppy.sh/beatmapsets?m=2">osu!catch</a><a class="beatmapsets-search-filter__item" data-filter-value="3" href="https://osu.ppy.sh/beatmapsets?m=3">osu!mania</a></div></div></div></div></div></div>
            </div>
            </div>
</div>
</div>



<div class="js-user-verification--reference"></div>

            <div class="osu-page osu-page--notification-banners js-notification-banners">
                            </div>
                <div class="osu-layout__section osu-layout__section--full js-content beatmaps_index">
                          <div class="js-react--beatmaps" data-advanced-search="1"><div class="header-v4 header-v4--beatmapsets"><div class="header-v4__container header-v4__container--main"><div class="header-v4__bg-container"><div class="header-v4__bg"></div></div><div class="header-v4__content"><div class="header-v4__row header-v4__row--title"><div class="header-v4__icon"></div><div class="header-v4__title">beatmap listing</div></div></div></div></div><div class="osu-page osu-page--beatmapsets-search-header"><div class="beatmapsets-search"><div class="beatmapsets-search__cover"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1800829/covers/cover.jpg?1661028344&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1800829/covers/cover@2x.jpg?1661028344&quot;);"></div></div><div class="beatmapsets-search__input-container"><input class="beatmapsets-search__input js-beatmapsets-search-input" name="search" placeholder="type in keywords..." value=""><div class="beatmapsets-search__icon"><i class="fas fa-search"></i></div></div><div class="beatmapsets-search-filter"><span class="beatmapsets-search-filter__header">General</span><div class="beatmapsets-search-filter__items"><a class="beatmapsets-search-filter__item" data-filter-value="recommended" href="https://osu.ppy.sh/beatmapsets?c=recommended">Recommended difficulty (1.00)</a><a class="beatmapsets-search-filter__item" data-filter-value="converts" href="https://osu.ppy.sh/beatmapsets?c=converts">Include converted beatmaps</a><a class="beatmapsets-search-filter__item" data-filter-value="follows" href="https://osu.ppy.sh/beatmapsets?c=follows">Subscribed mappers</a><a class="beatmapsets-search-filter__item" data-filter-value="spotlights" href="https://osu.ppy.sh/beatmapsets?c=spotlights">Spotlighted beatmaps</a><a class="beatmapsets-search-filter__item beatmapsets-search-filter__item--featured-artists" data-filter-value="featured_artists" href="https://osu.ppy.sh/beatmapsets?c=featured_artists">Featured artists</a></div></div><div class="beatmapsets-search-filter"><span class="beatmapsets-search-filter__header">Mode</span><div class="beatmapsets-search-filter__items"><a class="beatmapsets-search-filter__item beatmapsets-search-filter__item--active" href="https://osu.ppy.sh/beatmapsets">Any</a><a class="beatmapsets-search-filter__item" data-filter-value="0" href="https://osu.ppy.sh/beatmapsets?m=0">osu!</a><a class="beatmapsets-search-filter__item" data-filter-value="1" href="https://osu.ppy.sh/beatmapsets?m=1">osu!taiko</a><a class="beatmapsets-search-filter__item" data-filter-value="2" href="https://osu.ppy.sh/beatmapsets?m=2">osu!catch</a><a class="beatmapsets-search-filter__item" data-filter-value="3" href="https://osu.ppy.sh/beatmapsets?m=3">osu!mania</a></div></div><div class="beatmapsets-search-filter"><span class="beatmapsets-search-filter__header">Categories</span><div class="beatmapsets-search-filter__items"><a class="beatmapsets-search-filter__item" data-filter-value="any" href="https://osu.ppy.sh/beatmapsets?s=any">Any</a><a class="beatmapsets-search-filter__item beatmapsets-search-filter__item--active" data-filter-value="leaderboard" href="https://osu.ppy.sh/beatmapsets">Has Leaderboard</a><a class="beatmapsets-search-filter__item" data-filter-value="ranked" href="https://osu.ppy.sh/beatmapsets?s=ranked">Ranked</a><a class="beatmapsets-search-filter__item" data-filter-value="qualified" href="https://osu.ppy.sh/beatmapsets?s=qualified">Qualified</a><a class="beatmapsets-search-filter__item" data-filter-value="loved" href="https://osu.ppy.sh/beatmapsets?s=loved">Loved</a><a class="beatmapsets-search-filter__item" data-filter-value="favourites" href="https://osu.ppy.sh/beatmapsets?s=favourites">Favourites</a><a class="beatmapsets-search-filter__item" data-filter-value="pending" href="https://osu.ppy.sh/beatmapsets?s=pending">Pending</a><a class="beatmapsets-search-filter__item" data-filter-value="wip" href="https://osu.ppy.sh/beatmapsets?s=wip">WIP</a><a class="beatmapsets-search-filter__item" data-filter-value="graveyard" href="https://osu.ppy.sh/beatmapsets?s=graveyard">Graveyard</a><a class="beatmapsets-search-filter__item" data-filter-value="mine" href="https://osu.ppy.sh/beatmapsets?s=mine">My Maps</a></div></div><div class="beatmapsets-search-filter"><span class="beatmapsets-search-filter__header">Explicit Content</span><div class="beatmapsets-search-filter__items"><a class="beatmapsets-search-filter__item beatmapsets-search-filter__item--active" data-filter-value="false" href="https://osu.ppy.sh/beatmapsets">Hide</a><a class="beatmapsets-search-filter__item" data-filter-value="true" href="https://osu.ppy.sh/beatmapsets?nsfw=true">Show</a></div></div><a class="beatmapsets-search__expand-link" href="#"><div>More Search Options</div><div><i class="fas fa-angle-down"></i></div></a><div class="beatmapsets-search__advanced"><div class="beatmapsets-search-filter"><span class="beatmapsets-search-filter__header">Genre</span><div class="beatmapsets-search-filter__items"><a class="beatmapsets-search-filter__item beatmapsets-search-filter__item--active" href="https://osu.ppy.sh/beatmapsets">Any</a><a class="beatmapsets-search-filter__item" data-filter-value="1" href="https://osu.ppy.sh/beatmapsets?g=1">Unspecified</a><a class="beatmapsets-search-filter__item" data-filter-value="2" href="https://osu.ppy.sh/beatmapsets?g=2">Video Game</a><a class="beatmapsets-search-filter__item" data-filter-value="3" href="https://osu.ppy.sh/beatmapsets?g=3">Anime</a><a class="beatmapsets-search-filter__item" data-filter-value="4" href="https://osu.ppy.sh/beatmapsets?g=4">Rock</a><a class="beatmapsets-search-filter__item" data-filter-value="5" href="https://osu.ppy.sh/beatmapsets?g=5">Pop</a><a class="beatmapsets-search-filter__item" data-filter-value="6" href="https://osu.ppy.sh/beatmapsets?g=6">Other</a><a class="beatmapsets-search-filter__item" data-filter-value="7" href="https://osu.ppy.sh/beatmapsets?g=7">Novelty</a><a class="beatmapsets-search-filter__item" data-filter-value="9" href="https://osu.ppy.sh/beatmapsets?g=9">Hip Hop</a><a class="beatmapsets-search-filter__item" data-filter-value="10" href="https://osu.ppy.sh/beatmapsets?g=10">Electronic</a><a class="beatmapsets-search-filter__item" data-filter-value="11" href="https://osu.ppy.sh/beatmapsets?g=11">Metal</a><a class="beatmapsets-search-filter__item" data-filter-value="12" href="https://osu.ppy.sh/beatmapsets?g=12">Classical</a><a class="beatmapsets-search-filter__item" data-filter-value="13" href="https://osu.ppy.sh/beatmapsets?g=13">Folk</a><a class="beatmapsets-search-filter__item" data-filter-value="14" href="https://osu.ppy.sh/beatmapsets?g=14">Jazz</a></div></div><div class="beatmapsets-search-filter"><span class="beatmapsets-search-filter__header">Language</span><div class="beatmapsets-search-filter__items"><a class="beatmapsets-search-filter__item beatmapsets-search-filter__item--active" href="https://osu.ppy.sh/beatmapsets">Any</a><a class="beatmapsets-search-filter__item" data-filter-value="2" href="https://osu.ppy.sh/beatmapsets?l=2">English</a><a class="beatmapsets-search-filter__item" data-filter-value="4" href="https://osu.ppy.sh/beatmapsets?l=4">Chinese</a><a class="beatmapsets-search-filter__item" data-filter-value="7" href="https://osu.ppy.sh/beatmapsets?l=7">French</a><a class="beatmapsets-search-filter__item" data-filter-value="8" href="https://osu.ppy.sh/beatmapsets?l=8">German</a><a class="beatmapsets-search-filter__item" data-filter-value="11" href="https://osu.ppy.sh/beatmapsets?l=11">Italian</a><a class="beatmapsets-search-filter__item" data-filter-value="3" href="https://osu.ppy.sh/beatmapsets?l=3">Japanese</a><a class="beatmapsets-search-filter__item" data-filter-value="6" href="https://osu.ppy.sh/beatmapsets?l=6">Korean</a><a class="beatmapsets-search-filter__item" data-filter-value="10" href="https://osu.ppy.sh/beatmapsets?l=10">Spanish</a><a class="beatmapsets-search-filter__item" data-filter-value="9" href="https://osu.ppy.sh/beatmapsets?l=9">Swedish</a><a class="beatmapsets-search-filter__item" data-filter-value="12" href="https://osu.ppy.sh/beatmapsets?l=12">Russian</a><a class="beatmapsets-search-filter__item" data-filter-value="13" href="https://osu.ppy.sh/beatmapsets?l=13">Polish</a><a class="beatmapsets-search-filter__item" data-filter-value="5" href="https://osu.ppy.sh/beatmapsets?l=5">Instrumental</a><a class="beatmapsets-search-filter__item" data-filter-value="1" href="https://osu.ppy.sh/beatmapsets?l=1">Unspecified</a><a class="beatmapsets-search-filter__item" data-filter-value="14" href="https://osu.ppy.sh/beatmapsets?l=14">Other</a></div></div><div class="beatmapsets-search-filter"><span class="beatmapsets-search-filter__header">Extra</span><div class="beatmapsets-search-filter__items"><a class="beatmapsets-search-filter__item" data-filter-value="video" href="https://osu.ppy.sh/beatmapsets?e=video">Has Video</a><a class="beatmapsets-search-filter__item" data-filter-value="storyboard" href="https://osu.ppy.sh/beatmapsets?e=storyboard">Has Storyboard</a></div></div><div class="beatmapsets-search-filter"><span class="beatmapsets-search-filter__header">Rank Achieved</span><div class="beatmapsets-search-filter__items"><a class="beatmapsets-search-filter__item" data-filter-value="XH" href="https://osu.ppy.sh/beatmapsets?r=XH">Silver SS</a><a class="beatmapsets-search-filter__item" data-filter-value="X" href="https://osu.ppy.sh/beatmapsets?r=X">SS</a><a class="beatmapsets-search-filter__item" data-filter-value="SH" href="https://osu.ppy.sh/beatmapsets?r=SH">Silver S</a><a class="beatmapsets-search-filter__item" data-filter-value="S" href="https://osu.ppy.sh/beatmapsets?r=S">S</a><a class="beatmapsets-search-filter__item" data-filter-value="A" href="https://osu.ppy.sh/beatmapsets?r=A">A</a><a class="beatmapsets-search-filter__item" data-filter-value="B" href="https://osu.ppy.sh/beatmapsets?r=B">B</a><a class="beatmapsets-search-filter__item" data-filter-value="C" href="https://osu.ppy.sh/beatmapsets?r=C">C</a><a class="beatmapsets-search-filter__item" data-filter-value="D" href="https://osu.ppy.sh/beatmapsets?r=D">D</a></div></div><div class="beatmapsets-search-filter"><span class="beatmapsets-search-filter__header">Played</span><div class="beatmapsets-search-filter__items"><a class="beatmapsets-search-filter__item beatmapsets-search-filter__item--active" data-filter-value="any" href="https://osu.ppy.sh/beatmapsets">Any</a><a class="beatmapsets-search-filter__item" data-filter-value="played" href="https://osu.ppy.sh/beatmapsets?played=played">Played</a><a class="beatmapsets-search-filter__item" data-filter-value="unplayed" href="https://osu.ppy.sh/beatmapsets?played=unplayed">Unplayed</a></div></div></div></div></div><div class="js-sticky-header"></div><div class="osu-layout__row osu-layout__row--page-compact"><div class="beatmapsets"><div class="beatmapsets__toolbar"><div class="beatmapsets__toolbar-item"><div class="sort sort--beatmapsets"><div class="sort__items"><span class="sort__item sort__item--title">Sort by</span><a class="sort__item sort__item--button" data-field="title" href="#">Title<span class="sort__item-arrow"><i class="fas fa-caret-down"></i></span></a><a class="sort__item sort__item--button" data-field="artist" href="#">Artist<span class="sort__item-arrow"><i class="fas fa-caret-down"></i></span></a><a class="sort__item sort__item--button" data-field="difficulty" href="#">Difficulty<span class="sort__item-arrow"><i class="fas fa-caret-down"></i></span></a><a class="sort__item sort__item--button sort__item--active" data-field="ranked" href="#">Ranked<span class="sort__item-arrow"><i class="fas fa-caret-down"></i></span></a><a class="sort__item sort__item--button" data-field="rating" href="#">Rating<span class="sort__item-arrow"><i class="fas fa-caret-down"></i></span></a><a class="sort__item sort__item--button" data-field="plays" href="#">Plays<span class="sort__item-arrow"><i class="fas fa-caret-down"></i></span></a><a class="sort__item sort__item--button" data-field="favourites" href="#">Favourites<span class="sort__item-arrow"><i class="fas fa-caret-down"></i></span></a></div></div></div><div class="beatmapsets__toolbar-item"><div class="sort hidden-xs"><div class="sort__items"><button class="sort__item sort__item--active sort__item--button" type="button"><span class="fas fa-th"></span></button><button class="sort__item sort__item--button" type="button"><span class="fas fa-th-large"></span></button></div></div></div></div><div class="beatmapsets__content js-audio--group"><div style="box-sizing: border-box; height: 2750px; padding-top: 0px;"><div class="beatmapsets__items"><div class="beatmapsets__items-row"><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1800829.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1800829"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1800829/covers/list.jpg?1661028344&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1800829/covers/list@2x.jpg?1661028344&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1800829/covers/card.jpg?1661028344&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1800829/covers/card@2x.jpg?1661028344&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1800829">Tasogare no Odoriba</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1800829">by zakuro</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow">メメントモリ</div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="2667496" href="https://osu.ppy.sh/users/2667496" data-hasqtip="90">Kuro Fuyusaki</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" data-orig-title="Favourites: 41" data-hasqtip="91"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>41</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 3,199"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>3.2k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-28T04:24:56+00:00" title="2022-08-28T04:24:56+00:00">28 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1800829"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-osu"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(136, 254, 80);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(249, 213, 96);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(255, 92, 109);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(202, 70, 180);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(179, 78, 195);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1800829/download" title="download"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1824077.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1824077"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1824077/covers/list.jpg?1661049610&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1824077/covers/list@2x.jpg?1661049610&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1824077/covers/card.jpg?1661049610&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1824077/covers/card@2x.jpg?1661049610&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1824077">Girl's spirit -Otome no Kimochi-</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1824077">by Rita</a><div class="beatmapset-panel__badge-container"><span class="beatmapset-badge beatmapset-badge--featured-artist beatmapset-badge--panel">Featured artist</span></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow">屋上の百合霊さん</div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="10820856" href="https://osu.ppy.sh/users/10820856" data-hasqtip="89">Shirahane Suou</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 17"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>17</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 1,793"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>1.8k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-28T03:05:44+00:00" data-orig-title="2022-08-28T03:05:44+00:00" data-hasqtip="88">28 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1824077"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-osu"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(109, 255, 151);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(237, 242, 91);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(255, 109, 107);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(232, 74, 148);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1824077/download" title="download"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div></div><div class="beatmapsets__items-row"><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1629837.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1629837"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1629837/covers/list.jpg?1660874309&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1629837/covers/list@2x.jpg?1660874309&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1629837/covers/card.jpg?1660874309&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1629837/covers/card@2x.jpg?1660874309&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1629837">God-ish</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1629837">by kurokumo</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow"></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="7132267" href="https://osu.ppy.sh/users/7132267">Nelliel</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 347"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>347</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 10,428"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>10.4k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-28T01:02:38+00:00" title="2022-08-28T01:02:38+00:00">28 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1629837"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-osu"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(95, 255, 185);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(248, 220, 95);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(255, 96, 109);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(228, 74, 154);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(203, 70, 180);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(189, 73, 189);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(96, 95, 216);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1629837/download" title="download"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1809333.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1809333"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1809333/covers/list.jpg?1661405283&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1809333/covers/list@2x.jpg?1661405283&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1809333/covers/card.jpg?1661405283&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1809333/covers/card@2x.jpg?1661405283&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1809333">Rasputin</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1809333">by Boney M.</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow"></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="9562117" href="https://osu.ppy.sh/users/9562117" data-hasqtip="94">Aranel</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 52"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>52</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 3,862"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>3.9k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-28T00:02:13+00:00" title="2022-08-28T00:02:13+00:00">28 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1809333"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-osu"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(252, 175, 100);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1809333/download" data-orig-title="download" data-hasqtip="87"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div></div><div class="beatmapsets__items-row"><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1800982.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1800982"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1800982/covers/list.jpg?1661027138&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1800982/covers/list@2x.jpg?1661027138&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1800982/covers/card.jpg?1661027138&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1800982/covers/card@2x.jpg?1661027138&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"><div class="beatmapset-panel__play-icon" title="This beatmap contains video"><i class="fas fa-film"></i></div></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1800982">ALONES (TV Size)</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1800982">by Aqua Timez</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow">BLEACH</div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="2306637" href="https://osu.ppy.sh/users/2306637">Secre</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 12"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>12</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 816"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>816</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T21:46:22+00:00" title="2022-08-27T21:46:22+00:00">28 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1800982"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-fruits"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(79, 231, 232);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(99, 255, 177);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(225, 243, 89);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(253, 164, 101);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(255, 97, 109);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1800982/download" title="download with video"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1686490.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1686490"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1686490/covers/list.jpg?1661022975&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1686490/covers/list@2x.jpg?1661022975&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1686490/covers/card.jpg?1661022975&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1686490/covers/card@2x.jpg?1661022975&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1686490">Txxs or get the fxxk out!!</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1686490">by Morimori Atsushi</a><div class="beatmapset-panel__badge-container"><span class="beatmapset-badge beatmapset-badge--featured-artist beatmapset-badge--panel">Featured artist</span></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow">東方神霊廟　～ Ten Desires.</div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="2688581" href="https://osu.ppy.sh/users/2688581" data-hasqtip="92">Luscent</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 68"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>68</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 8,243"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>8.2k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T19:42:55+00:00" title="2022-08-27T19:42:55+00:00">27 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1686490"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-osu"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(179, 250, 84);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(250, 196, 98);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(231, 74, 150);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(199, 69, 183);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(153, 87, 206);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(89, 87, 205);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(71, 69, 182);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1686490/download" title="download"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div></div><div class="beatmapsets__items-row"><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1769191.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1769191"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1769191/covers/list.jpg?1661013582&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1769191/covers/list@2x.jpg?1661013582&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1769191/covers/card.jpg?1661013582&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1769191/covers/card@2x.jpg?1661013582&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"><div class="beatmapset-panel__play-icon" title="This beatmap contains video"><i class="fas fa-film"></i></div></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1769191">Moon Halo</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1769191">by HOYO-MiX feat. Chalili, TetraCalyx, Hanser</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow">崩坏3</div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="9778431" href="https://osu.ppy.sh/users/9778431">eIis</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 50"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>50</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 2,983"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>3k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T17:26:40+00:00" title="2022-08-27T17:26:40+00:00">27 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1769191"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-osu"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(79, 254, 214);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(182, 250, 84);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(253, 157, 102);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1769191/download" title="download with video"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1684406.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1684406"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1684406/covers/list.jpg?1661495438&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1684406/covers/list@2x.jpg?1661495438&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1684406/covers/card.jpg?1661495438&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1684406/covers/card@2x.jpg?1661495438&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1684406">Cosmo Station</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1684406">by seatrus</a><div class="beatmapset-panel__badge-container"><span class="beatmapset-badge beatmapset-badge--featured-artist beatmapset-badge--panel">Featured artist</span></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow"></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="2218047" href="https://osu.ppy.sh/users/2218047" data-hasqtip="95">Kim_GodSSI</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 29"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>29</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" data-orig-title="Playcount: 372" data-hasqtip="96"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>372</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T16:45:25+00:00" title="2022-08-27T16:45:25+00:00">27 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1684406"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-mania"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(14, 12, 80);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1684406/download" title="download"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div></div><div class="beatmapsets__items-row"><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1752096.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1752096"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1752096/covers/list.jpg?1660934612&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1752096/covers/list@2x.jpg?1660934612&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1752096/covers/card.jpg?1660934612&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1752096/covers/card@2x.jpg?1660934612&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1752096">MORE &amp; MORE</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1752096">by Momo Belia Deviluke (CV: Toyosaki Aki)</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow">To LOVEる-とらぶる-ダークネス</div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="9704802" href="https://osu.ppy.sh/users/9704802">Zekk</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 19"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>19</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 4,329"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>4.3k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T16:42:29+00:00" title="2022-08-27T16:42:29+00:00">27 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1752096"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-osu"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(118, 255, 114);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(251, 184, 99);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(247, 77, 126);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(216, 72, 167);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(180, 78, 194);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1752096/download" title="download"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1804171.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1804171"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1804171/covers/list.jpg?1660572206&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1804171/covers/list@2x.jpg?1660572206&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1804171/covers/card.jpg?1660572206&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1804171/covers/card@2x.jpg?1660572206&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1804171">forever we can make it!</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1804171">by THYME</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow">To LOVEる -とらぶる-</div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="9704802" href="https://osu.ppy.sh/users/9704802">Zekk</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 21"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>21</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 3,222"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>3.2k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T16:27:41+00:00" title="2022-08-27T16:27:41+00:00">27 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1804171"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-osu"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(250, 204, 97);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(253, 78, 114);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(229, 74, 152);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(224, 73, 159);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1804171/download" title="download"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div></div><div class="beatmapsets__items-row"><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1788259.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1788259"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1788259/covers/list.jpg?1661517986&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1788259/covers/list@2x.jpg?1661517986&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1788259/covers/card.jpg?1661517986&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1788259/covers/card@2x.jpg?1661517986&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1788259">Anima Libera (Strong Edit) (Nightcore &amp; Cut Ver.)</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1788259">by EMI</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow"></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="4452992" href="https://osu.ppy.sh/users/4452992">Sotarks</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 42"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>42</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 8,761"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>8.8k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T16:26:39+00:00" title="2022-08-27T16:26:39+00:00">27 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1788259"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-osu"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(114, 255, 134);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(250, 200, 98);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(255, 113, 107);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(220, 72, 163);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1788259/download" title="download"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1797642.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1797642"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1797642/covers/list.jpg?1660939132&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1797642/covers/list@2x.jpg?1660939132&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1797642/covers/card.jpg?1660939132&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1797642/covers/card@2x.jpg?1660939132&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1797642">DJ Majokko Mirakurun [ Producer Mix ] [ Nightcore ]</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1797642">by DJ Majokko Mirakurun</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow"></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="3196091" href="https://osu.ppy.sh/users/3196091">Genjuro</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 57"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>57</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 178"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>178</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T15:42:12+00:00" title="2022-08-27T15:42:12+00:00">27 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1797642"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-taiko"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(44, 42, 154);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1797642/download" title="download"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div></div><div class="beatmapsets__items-row"><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1287129.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1287129"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1287129/covers/list.jpg?1660853250&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1287129/covers/list@2x.jpg?1660853250&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1287129/covers/card.jpg?1660853250&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1287129/covers/card@2x.jpg?1660853250&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1287129">Schranz Shot</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1287129">by Active Planets</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow">穢翼のユースティア</div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="2446000" href="https://osu.ppy.sh/users/2446000">richardfeder</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 8"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>8</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 560"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>560</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T14:04:56+00:00" title="2022-08-27T14:04:56+00:00">27 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1287129"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-mania"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(79, 249, 218);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(186, 249, 85);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(248, 218, 95);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(255, 100, 108);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1287129/download" title="download"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1793369.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1793369"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1793369/covers/list.jpg?1660478268&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1793369/covers/list@2x.jpg?1660478268&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1793369/covers/card.jpg?1660478268&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1793369/covers/card@2x.jpg?1660478268&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1793369">Black Hole</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1793369">by OPFuture</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow"></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="2123087" href="https://osu.ppy.sh/users/2123087">hehe</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 55"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>55</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 6,292"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>6.3k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T10:02:11+00:00" title="2022-08-27T10:02:11+00:00">27 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1793369"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-osu"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(154, 252, 81);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(247, 233, 93);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(255, 111, 107);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(255, 98, 109);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(207, 70, 176);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1793369/download" title="download"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div></div><div class="beatmapsets__items-row"><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1813130.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1813130"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1813130/covers/list.jpg?1660582696&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1813130/covers/list@2x.jpg?1660582696&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1813130/covers/card.jpg?1660582696&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1813130/covers/card@2x.jpg?1660582696&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1813130">Wasureji no Kotonoha</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1813130">by Ashimine Kiwako</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow">グリムノーツ</div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="2043401" href="https://osu.ppy.sh/users/2043401">Enon</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 35"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>35</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 2,819"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>2.8k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T06:46:23+00:00" title="2022-08-27T06:46:23+00:00">27 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1813130"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-osu"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(191, 248, 85);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(255, 122, 105);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1813130/download" title="download"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1612932.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1612932"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1612932/covers/list.jpg?1660956474&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1612932/covers/list@2x.jpg?1660956474&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1612932/covers/card.jpg?1660956474&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1612932/covers/card@2x.jpg?1660956474&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"><div class="beatmapset-panel__play-icon" title="This beatmap contains video"><i class="fas fa-film"></i></div></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1612932">theyaremanycolors</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1612932">by Frums</a><div class="beatmapset-panel__badge-container"><span class="beatmapset-badge beatmapset-badge--featured-artist beatmapset-badge--panel">Featured artist</span></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow">BOFU2017 - LEGENDA EST A MYTH -</div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="702598" href="https://osu.ppy.sh/users/702598">Spectator</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 23"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>23</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 1,766"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>1.8k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T06:03:32+00:00" title="2022-08-27T06:03:32+00:00">27 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1612932"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-fruits"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(117, 255, 121);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(222, 244, 89);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(255, 118, 106);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(194, 71, 186);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(80, 78, 193);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1612932/download" title="download with video"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div></div><div class="beatmapsets__items-row"><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1816401.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1816401"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1816401/covers/list.jpg?1660828324&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1816401/covers/list@2x.jpg?1660828324&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1816401/covers/card.jpg?1660828324&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1816401/covers/card@2x.jpg?1660828324&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1816401">Apocalypse</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1816401">by Gram vs. Yooh</a><div class="beatmapset-panel__badge-container"><span class="beatmapset-badge beatmapset-badge--featured-artist beatmapset-badge--panel">Featured artist</span></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow"></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="7890134" href="https://osu.ppy.sh/users/7890134">Jemzuu</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 22"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>22</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 2,122"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>2.1k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T05:22:06+00:00" title="2022-08-27T05:22:06+00:00">27 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1816401"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-fruits"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(79, 244, 222);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(129, 255, 79);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(249, 216, 96);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(255, 103, 108);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(201, 69, 181);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(99, 97, 219);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(51, 49, 161);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1816401/download" title="download"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1781620.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1781620"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1781620/covers/list.jpg?1660851627&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1781620/covers/list@2x.jpg?1660851627&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1781620/covers/card.jpg?1660851627&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1781620/covers/card@2x.jpg?1660851627&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"><div class="beatmapset-panel__play-icon" title="This beatmap contains storyboard"><i class="fas fa-image"></i></div></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1781620">Glory Days</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1781620">by Fellowship</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow"></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="14729352" href="https://osu.ppy.sh/users/14729352">nebuwua</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 285"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>285</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 64,966"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>65k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T03:43:10+00:00" title="2022-08-27T03:43:10+00:00">27 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1781620"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-osu"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(252, 77, 118);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(183, 76, 192);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(96, 95, 216);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(67, 65, 178);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1781620/download" title="download"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div></div><div class="beatmapsets__items-row"><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1827862.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1827862"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1827862/covers/list.jpg?1660918098&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1827862/covers/list@2x.jpg?1660918098&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1827862/covers/card.jpg?1660918098&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1827862/covers/card@2x.jpg?1660918098&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"><div class="beatmapset-panel__play-icon" title="This beatmap contains video"><i class="fas fa-film"></i></div></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1827862">Izzy's Got the Frizzies (TV Size)</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1827862">by Carmen Carter</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow">Phineas and Ferb</div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="3181083" href="https://osu.ppy.sh/users/3181083">AJT</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 16"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>16</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 5,889"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>5.9k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T01:22:46+00:00" title="2022-08-27T01:22:46+00:00">27 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1827862"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-osu"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(113, 255, 137);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(195, 248, 86);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(249, 208, 96);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1827862/download" title="download with video"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div><div class="beatmapsets__item"><div class="beatmapset-panel beatmapset-panel--size-normal js-audio--player" data-audio-url="//b.ppy.sh/preview/1475460.mp3" style="--beatmaps-popup-transition-duration:150ms;"><a class="beatmapset-panel__cover-container" href="https://osu.ppy.sh/beatmapsets/1475460"><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--play"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1475460/covers/list.jpg?1660938038&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1475460/covers/list@2x.jpg?1660938038&quot;);"></div></div><div class="beatmapset-panel__cover-col beatmapset-panel__cover-col--info"><div class="beatmapset-cover beatmapset-cover--full" style="--bg:url(&quot;https://assets.ppy.sh/beatmaps/1475460/covers/card.jpg?1660938038&quot;); --bg-2x:url(&quot;https://assets.ppy.sh/beatmaps/1475460/covers/card@2x.jpg?1660938038&quot;);"></div></div></a><div class="beatmapset-panel__content"><div class="beatmapset-panel__play-container"><button class="beatmapset-panel__play js-audio--play" type="button"><span class="play-button"></span></button><div class="beatmapset-panel__play-progress"><div class="circular-progress circular-progress--beatmapset-panel" title="0 / 1"><div class="circular-progress__label">1</div><div class="circular-progress__slice"><div class="circular-progress__circle"></div><div class="circular-progress__circle circular-progress__circle--fill"></div></div></div></div><div class="beatmapset-panel__play-icons"></div></div><div class="beatmapset-panel__info"><div class="beatmapset-panel__info-row beatmapset-panel__info-row--title"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1475460">Toumei Datta Sekai (TV Size)</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--artist"><a class="beatmapset-panel__main-link u-ellipsis-overflow" href="https://osu.ppy.sh/beatmapsets/1475460">by Hata Motohiro</a></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--source"><div class="u-ellipsis-overflow">NARUTO-ナルト-疾風伝</div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--mapper"><div class="u-ellipsis-overflow">mapped by <a class="js-usercard beatmapset-panel__mapper-link u-hover" data-user-id="13570072" href="https://osu.ppy.sh/users/13570072">Leon Brigido</a></div></div><div class="beatmapset-panel__info-row beatmapset-panel__info-row--stats"><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--favourite-count" title="Favourites: 31"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw far fa-heart"></i></span><span>31</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--play-count" title="Playcount: 2,423"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-play-circle"></i></span><span>2.4k</span></div><div class="beatmapset-panel__stats-item beatmapset-panel__stats-item--date"><span class="beatmapset-panel__stats-item-icon"><i class="fa-fw fas fa-check-circle"></i></span><time class="js-tooltip-time" datetime="2022-08-27T01:01:53+00:00" title="2022-08-27T01:01:53+00:00">27 Aug 2022</time></div></div><a class="beatmapset-panel__info-row beatmapset-panel__info-row--extra" href="https://osu.ppy.sh/beatmapsets/1475460"><div class="beatmapset-panel__extra-item"><div class="beatmapset-status beatmapset-status--panel" style="--bg:var(--beatmapset-ranked-bg); --colour:var(--beatmapset-ranked-colour);">Ranked</div></div><div class="beatmapset-panel__extra-item beatmapset-panel__extra-item--dots"><div class="beatmapset-panel__beatmap-icon"><i class="fal fa-extra-mode-mania"></i></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(79, 196, 253);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(79, 240, 225);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(146, 253, 81);"></div><div class="beatmapset-panel__beatmap-dot" style="--bg:rgb(248, 226, 94);"></div></div></a></div><div class="beatmapset-panel__menu-container"><div class="beatmapset-panel__menu"><button class="beatmapset-panel__menu-item" title="Favourite this beatmap" type="button"><span class="far fa-heart"></span></button><a class="beatmapset-panel__menu-item" data-turbolinks="false" href="https://osu.ppy.sh/beatmapsets/1475460/download" title="download"><span class="fas fa-file-download"></span></a></div></div></div><button class="beatmapset-panel__mobile-expand" type="button"><span class="fas fa-angle-down"></span></button></div></div></div></div></div></div><div class="beatmapsets__paginator"><div></div><button type="button" class="show-more-link show-more-link--beatmapsets"><span class="show-more-link__spinner"><div class="la-ball-clip-rotate"></div></span><span class="show-more-link__label"><span class="show-more-link__label-icon show-more-link__label-icon--left"><span class="fas fa-angle-down"></span></span><span class="show-more-link__label-text">show more</span><span class="show-more-link__label-icon show-more-link__label-icon--right"><span class="fas fa-angle-down"></span></span></span></button></div></div></div><button class="back-to-top" data-tooltip-float="fixed" title="Back to top"><i class="fas fa-angle-up"></i></button></div>
  
        </div>
                    <!-- Root element of PhotoSwipe. Must have class pswp. -->
<div class="pswp" tabindex="-1" role="dialog" aria-hidden="true">

    <!-- Background of PhotoSwipe.
         It's a separate element as animating opacity is faster than rgba(). -->
    <div class="pswp__bg"></div>

    <!-- Slides wrapper with overflow:hidden. -->
    <div class="pswp__scroll-wrap">

        <!-- Container that holds slides.
            PhotoSwipe keeps only 3 of them in the DOM to save memory.
            Don't modify these 3 pswp__item elements, data is added later on. -->
        <div class="pswp__container">
            <div class="pswp__item"></div>
            <div class="pswp__item"></div>
            <div class="pswp__item"></div>
        </div>

        <!-- Default (PhotoSwipeUI_Default) interface on top of sliding area. Can be changed. -->
        <div class="pswp__ui pswp__ui--hidden">

            <div class="pswp__top-bar">

                <!--  Controls are self-explanatory. Order can be changed. -->

                <div class="pswp__counter"></div>

                <button type="button" class="pswp__button pswp__button--close" title="Close (Esc)"></button>

                <button type="button" class="pswp__button pswp__button--fs" title="Toggle fullscreen"></button>

                <button type="button" class="pswp__button pswp__button--zoom" title="Zoom in/out"></button>

                <div class="js-pswp-buttons"></div>

                <!-- Preloader demo http://codepen.io/dimsemenov/pen/yyBWoR -->
                <!-- element will get modifier active when preloader is running -->
                <div class="pswp__preloader">
                    <div class="pswp__preloader__icn">
                      <div class="pswp__preloader__cut">
                        <div class="pswp__preloader__donut"></div>
                      </div>
                    </div>
                </div>
            </div>

            <div class="pswp__share-modal pswp__share-modal--hidden pswp__single-tap">
                <div class="pswp__share-tooltip"></div>
            </div>

            <button type="button" class="pswp__button pswp__button--arrow--left" title="Previous (arrow left)">
            </button>

            <button type="button" class="pswp__button pswp__button--arrow--right" title="Next (arrow right)">
            </button>

            <div class="pswp__caption">
                <div class="pswp__caption__center"></div>
            </div>

        </div>

    </div>

</div>
            <footer class="no-print footer">
            <div class="footer__row">
                            <a class="footer__link" href="https://osu.ppy.sh/legal/en/Terms">
                    Terms
                </a>
                            <a class="footer__link" href="https://osu.ppy.sh/legal/en/Privacy">
                    Privacy
                </a>
                            <a class="footer__link" href="https://osu.ppy.sh/legal/en/Copyright">
                    Copyright (DMCA)
                </a>
                            <a class="footer__link" href="https://status.ppy.sh">
                    Server Status
                </a>
                            <a class="footer__link" href="https://github.com/ppy">
                    Source Code
                </a>
            
                    </div>
        <div class="footer__row">ppy powered 2007-2022</div>

    <div class="js-sync-height--target" data-sync-height-id="permanent-fixed-footer" style="min-height: 0px;"></div>
</footer>
        
        <div class="fixed-bar
                js-fixed-element
                js-fixed-bottom-bar
                js-sticky-footer--fixed-bar">
            <div class="js-permanent-fixed-footer
                    js-sync-height--reference" data-sync-height-target="permanent-fixed-footer">
                
                            </div>
        </div>

        <div id="main-player" class="audio-player-floating" data-turbolinks-permanent="">
            <div class="audio-player audio-player--main" data-audio-autoplay="0" data-audio-has-duration="1" data-audio-state="paused" data-audio-time-format="minute_minimal" data-audio-volume-bar-visible="1" data-audio-volume="quiet" data-audio-has-prev="0" data-audio-has-next="0" style="--duration:&quot;0:10&quot;; --volume:0.2; --current-time:&quot;0:00&quot;; --progress:0;" data-audio-visible="0" data-audio-over50="0">
    <button type="button" class="audio-player__button audio-player__button--prev js-audio--nav" data-audio-nav="prev"><span class="fas fa-fw fa-step-backward"></span></button>

    <button type="button" class="audio-player__button audio-player__button--play js-audio--main-play"><span class="fa-fw play-button"></span></button>

    <button type="button" class="audio-player__button audio-player__button--next js-audio--nav" data-audio-nav="next"><span class="fas fa-fw fa-step-forward"></span></button>

    <div class="audio-player__bar audio-player__bar--progress js-audio--seek">
      <div class="audio-player__bar-current"></div>
    </div>

    <div class="audio-player__timestamps">
      <div class="audio-player__timestamp audio-player__timestamp--current"></div>
      <div class="audio-player__timestamp-separator">/</div>
      <div class="audio-player__timestamp audio-player__timestamp--total"></div>
    </div>

    <div class="audio-player__volume-control">
      <button type="button" class="audio-player__volume-button js-audio--toggle-mute"></button>
      <div class="audio-player__bar audio-player__bar--volume js-audio--volume">
        <div class="audio-player__bar-current"></div>
      </div>
    </div>

    <div class="audio-player__autoplay-control">
      <button type="button" class="audio-player__autoplay-button js-audio--toggle-autoplay" title="Play next track automatically"></button>
    </div>
  </div>
            <div class="js-sync-height--target" data-sync-height-id="permanent-fixed-footer" style="min-height: 0px;"></div>
        </div>
        
        <div id="estimate-min-lines" class="estimate-min-lines" data-turbolinks-permanent="">
            <div class="estimate-min-lines__content js-estimate-min-lines"><div class="osu-md osu-md--comment"><p class="osu-md__paragraph">osu!radio has an increasingly nonzero chance of rickrolling me at any given point in time</p>
</div></div>
        </div>
        <script data-turbolinks-eval="always">
    var csrf = "UmOroUKsHiodxZ5qL206R3Fvhzl0G0Bo6viZl0ZO";
    var canonicalUrl = "";
</script>



<div id="js-usercard__loading-template" class="hidden">
    
    <div class="js-react--user-card"><div class="user-card user-card--highlightable user-card--card"><div class="user-card__background-overlay"></div><div class="user-card__card"><div class="user-card__content user-card__content--details"><div class="user-card__user"><div class="user-card__avatar-space"><div class="user-card__avatar-spinner"></div></div></div><div class="user-card__details"><div class="user-card__username-row"><div class="user-card__username u-ellipsis-pre-overflow">Loading...</div><div class="user-card__group-badges"></div></div></div></div></div></div></div>
</div>
        <div class="loading-overlay js-loading-overlay">
    <div class="loading-overlay__container">
                    <div class="loading-overlay__follow-point
                    loading-overlay__follow-point--1">
                ›
            </div>

                            <div class="loading-overlay__circle
                        loading-overlay__circle--1
                        loading-overlay__circle--approach"></div>
                            <div class="loading-overlay__circle
                        loading-overlay__circle--1
                        loading-overlay__circle--hit"></div>
                                <div class="loading-overlay__follow-point
                    loading-overlay__follow-point--2">
                ›
            </div>

                            <div class="loading-overlay__circle
                        loading-overlay__circle--2
                        loading-overlay__circle--approach"></div>
                            <div class="loading-overlay__circle
                        loading-overlay__circle--2
                        loading-overlay__circle--hit"></div>
                                <div class="loading-overlay__follow-point
                    loading-overlay__follow-point--3">
                ›
            </div>

                            <div class="loading-overlay__circle
                        loading-overlay__circle--3
                        loading-overlay__circle--approach"></div>
                            <div class="loading-overlay__circle
                        loading-overlay__circle--3
                        loading-overlay__circle--hit"></div>
                                <div class="loading-overlay__follow-point
                    loading-overlay__follow-point--4">
                ›
            </div>

                            <div class="loading-overlay__circle
                        loading-overlay__circle--4
                        loading-overlay__circle--approach"></div>
                            <div class="loading-overlay__circle
                        loading-overlay__circle--4
                        loading-overlay__circle--hit"></div>
                        </div>
</div>
        <div id="popup-container">
    <div class="alert alert-dismissable popup-clone col-md-6 col-md-offset-3 text-center" style="display: none">
        <button type="button" data-dismiss="alert" class="close"><i class="fas fa-times"></i></button>
        <span class="popup-text"></span>
    </div>
    <div class="empty-popup empty-popup--clone" style="display: none">
        <div class="popup-content"></div>
    </div>
</div>

        <script id="json-route-section" type="application/json">
            {"action":"index","controller":"beatmapsets_controller","namespace":"main","section":"beatmaps"}
        </script>

              
    <div class="js-user-verification modal fade" tabindex="-1">
        <div class="modal-dialog modal-dialog--full">
            <div class="user-verification-popup">
                <div class="osu-layout__row">
                    <div class="user-verification-popup__modal">
                        <div class="js-user-verification--box user-verification-popup__box">
                                                    </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

  <script id="json-filters" type="application/json">
    {"extras":[{"id":"video","name":"Has Video"},{"id":"storyboard","name":"Has Storyboard"}],"general":[{"id":"recommended","name":"Recommended difficulty"},{"id":"converts","name":"Include converted beatmaps"},{"id":"follows","name":"Subscribed mappers"},{"id":"spotlights","name":"Spotlighted beatmaps"},{"id":"featured_artists","name":"Featured artists"}],"genres":[{"id":null,"name":"Any"},{"id":1,"name":"Unspecified"},{"id":2,"name":"Video Game"},{"id":3,"name":"Anime"},{"id":4,"name":"Rock"},{"id":5,"name":"Pop"},{"id":6,"name":"Other"},{"id":7,"name":"Novelty"},{"id":9,"name":"Hip Hop"},{"id":10,"name":"Electronic"},{"id":11,"name":"Metal"},{"id":12,"name":"Classical"},{"id":13,"name":"Folk"},{"id":14,"name":"Jazz"}],"languages":[{"id":null,"name":"Any"},{"id":2,"name":"English"},{"id":4,"name":"Chinese"},{"id":7,"name":"French"},{"id":8,"name":"German"},{"id":11,"name":"Italian"},{"id":3,"name":"Japanese"},{"id":6,"name":"Korean"},{"id":10,"name":"Spanish"},{"id":9,"name":"Swedish"},{"id":12,"name":"Russian"},{"id":13,"name":"Polish"},{"id":5,"name":"Instrumental"},{"id":1,"name":"Unspecified"},{"id":14,"name":"Other"}],"modes":[{"id":null,"name":"Any"},{"id":0,"name":"osu!"},{"id":1,"name":"osu!taiko"},{"id":2,"name":"osu!catch"},{"id":3,"name":"osu!mania"}],"nsfw":[{"id":false,"name":"Hide"},{"id":true,"name":"Show"}],"played":[{"id":"any","name":"Any"},{"id":"played","name":"Played"},{"id":"unplayed","name":"Unplayed"}],"ranks":[{"id":"XH","name":"Silver SS"},{"id":"X","name":"SS"},{"id":"SH","name":"Silver S"},{"id":"S","name":"S"},{"id":"A","name":"A"},{"id":"B","name":"B"},{"id":"C","name":"C"},{"id":"D","name":"D"}],"statuses":[{"id":"any","name":"Any"},{"id":"leaderboard","name":"Has Leaderboard"},{"id":"ranked","name":"Ranked"},{"id":"qualified","name":"Qualified"},{"id":"loved","name":"Loved"},{"id":"favourites","name":"Favourites"},{"id":"pending","name":"Pending"},{"id":"wip","name":"WIP"},{"id":"graveyard","name":"Graveyard"},{"id":"mine","name":"My Maps"}]}
  </script>

  

  <div class="hidden js-react-turbolinks--script" data-src="/assets/js/beatmaps.f0ed6af8.js"></div>
    

</body></html>"""


# print(song_link)

soup = BeautifulSoup(code, 'lxml')
# print(request.text)

# .find('div', class_="osu-layout__row osu-layout__row--page-compact").find('div', class_='beatmapsets__items')
main_songs_container = soup.find('div', class_='osu-layout__section osu-layout__section--full js-content beatmaps_index')
# print(main_songs_container)
for i in range(1):
    song_container = main_songs_container.find_all('div', class_='beatmapsets__item')[i]
    name_container = song_container.find('div', class_='beatmapset-panel__content')\
        .find('div', class_='beatmapset-panel__info')\
            .find('div', class_='beatmapset-panel__info-row beatmapset-panel__info-row--title')
    name = name_container.find('a', class_='beatmapset-panel__info-row beatmapset-panel__info-row--title')
    link = name_container.get('href')
    print(f"Song name: {name}")
    print(f"Downloading link: {link}")

print(request)

        <header id="topnav">

            <!-- Topbar Start -->
            <div class="navbar-custom">
                <div class="container-fluid">
                    <div class="p-3 d-flex justify-content-center">
                        <div><h2 style="color: white;"> DEEP LEARNING COVID SPREAD</h2></div>
                    </div>
                </div> <!-- end container-fluid-->
            </div>
            <!-- end Topbar -->

            <div class="topbar-menu">
                <div class="container-fluid">
                    <div id="navigation">
                        <!-- Navigation Menu-->
                        <ul class="navigation-menu">

                            <li class="has-submenu">
                                <a href="#"> <i class="mdi mdi-chart-donut-variant"></i>PREDICTION AVEC MODELE PRE-ENTRAINNE <div class="arrow-down"></div></a>
                                <ul class="submenu">
                                    <li>
                                        <a href="{{route('confinement')}}">CONFINEMENT</a>
                                    </li>
                                    <li>
                                        <a href="{{route('deconfinement')}}">DECONFINEMENT</a>
                                    </li>
                                    <li>
                                        <a href="{{route('hybride')}}">HYBRIDE</a>
                                    </li>
                                </ul>
                            </li>
                            <li class="has-submenu">
                                <a href="{{route('entrainer')}}"> <i class="mdi mdi-google-circles-group"></i>ENTRAINNER VOTRE MODELE</a>
                            </li>

                            <li class="has-submenu">
                                <a href="{{route('info')}}"> <i class="mdi mdi-comment-alert"></i>INFORMATIONS A SAVOIR</a>
                            </li>

                        </ul>
                        <!-- End navigation menu -->

                        <div class="clearfix"></div>
                    </div>
                    <!-- end #navigation -->
                </div>
                <!-- end container -->
            </div>
            <!-- end navbar-custom -->

        </header>
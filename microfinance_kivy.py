kv="""
<MagicButton@MagicBehavior+MDRectangleFlatButton>
<Login>
    name:'login'
    MDBoxLayout:
        orientation:'horizontal'
        canvas:
            Color:
                rgba:(246/255,206/255,103/255,100)
            Rectangle:
                pos: (0,0)
                size: self.size
        MDBoxLayout:
            MDCard:
                radius: 36
                md_bg_color: "grey"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .4, 1
                FitImage:
                    size_hint_y: 1
                    pos_hint: {"top": 1}
                    source: 'image/cadre2.png'

        MDRelativeLayout:
            MDBoxLayout:
                orientation:'vertical'
                BoxLayout:
                    orientation:'horizontal'
                    size_hint_y: 1
                    height: self.minimum_height
                MDLabel:
                    text:"Connexion"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    halign:'center'
                    theme_text_color:"Custom"
                    text_color:1, 1, 1, 1
                    font_style:'H2'
                    font_name:'font\Gotu-Regular.ttf'
                    bold: True

                BoxLayout:
                    orientation:'horizontal'
                    size_hint_y: 1
                    height: self.minimum_height
                    MDLabel:
                        text:"Pseudo"
                        halign:'center'
                        theme_text_color:"Custom"
                        text_color:1, 1, 1, 1
                        font_style:'H5'
                        font_name:'font\Gotu-Regular.ttf'
                        bold: True
                    AnchorLayout:
                        
                        anchor_x:'left'
                        anchor_y:'center'
                        size_hint_y: 1
                        size_hint_x: 1 
                        MDTextField:
                            id:pseudocon
                            width: "300dp"
                            hint_text: "Nom d'utilisateur"
                            icon_left: "account-circle"
                            mode: "round"
                            size_hint_x: None
                BoxLayout:
                    orientation:'horizontal'
                    size_hint_y: 1
                    height: self.minimum_height
                    MDLabel:
                        text:"Mot de passe"
                        halign:'center'
                        theme_text_color:"Custom"
                        text_color:1, 1, 1, 1
                        font_style:'H5'
                        font_name:'font\Gotu-Regular.ttf'
                        bold: True
                    AnchorLayout:
                        
                        anchor_x:'left'
                        anchor_y:'center'
                        size_hint_y: 1
                        size_hint_x: 1 
                        MDTextField:
                            id: mdpcon
                            width: "300dp"
                            hint_text: "Mot de passe"
                            mode: "round"
                            password: True
                            icon_left: "key-variant"
                            size_hint_x: None
                            size_hint_y: None
                            pos_hint: {"center_x": .5, "center_y": .5}
                BoxLayout:
                    orientation:'horizontal'
                    size_hint_y: 1
                    height: self.minimum_height
                    
                        
                BoxLayout:
                    orientation:'horizontal'
                    size_hint_y: 1
                    height: self.minimum_height
                    BoxLayout:
                        orientation:'horizontal'
                        size_hint_y: 1
                        size_hint_x: .1
                        height: self.minimum_height
                    MDLabel:
                        text:"Vous n'avez pas de compte ?"
                        halign:'left'
                        theme_text_color:"Secondary"
                        text_color:(0/255,0/255,0/255,100)
                        bold: True
                        font_name:'font\Gotu-Regular.ttf'
                    
            MagicButton:
                id:btncon
                pos:400,180
                text: "    Se connecter    "
                text_color: "black"
                line_color: "black"
                on_release: 
                    self.grow()
                    app.seconnecter()
                font_name:'font\Gotu-Regular.ttf'
                md_bg_color:(255/255,255/255,255/255,100)
            MDTextButton:
                id:btninscrit
                pos:460,48
                text: "Cliquez ici"
                font_name:'font\Gotu-Regular.ttf'
                theme_text_color: "Custom"
                custom_color:(0/255,0/255,0/255,100)
                bold: True
                on_press:
                    root.manager.current='inscription'
            MDIconButton:
                icon: "eye-off"
                pos:584,287
                theme_text_color: "Hint"
                on_release:
                    self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                    mdpcon.password = False if mdpcon.password is True else True
<Inscription>
    name:'inscription'
    MDCard:
        size_hint: .7, .8
        radius: 5,20,60,20
        md_bg_color: "#F6CE67FF"
        pos_hint: {"center_x": .5, "center_y": .5}
        BoxLayout:
            orientation:'vertical'
            
            
            MDLabel:
                size_hint_y: 2
                text:"CREER VOTRE COMPTE"
                halign:'center'
                theme_text_color:"Custom"
                text_color:1, 1, 1, 1
                font_style:'H3'
                font_name:'font\Gotu-Regular.ttf'
                bold: True
                

            BoxLayout:
                orientation:'horizontal'
                
                BoxLayout:
                    orientation:'horizontal'
                    
                    MDLabel:
                        text:"Nom:"
                        size_hint_y: 1
                        halign:'center'
                        theme_text_color:"Custom"
                        text_color: 1, 1, 1, 1
                        font_style:'H6'
                        font_name:'font\Gotu-Regular.ttf'
                    

                    MDTextField:
                        id: nom_inscri
                        width: "100dp"
                        mode: "round"
                        size_hint_x: 1.5
                        md_bg_color:(217/255,217/255,217/255,100)
                        size_hint_y: None
                        pos_hint: {"center_x": 0, "center_y": .5}
                        
                
                BoxLayout:
                    orientation:'horizontal'
                
                    MDLabel:
                        text:"Pseudo:"
                        size_hint_y: 1
                        halign:'center'
                        theme_text_color:"Custom"
                        text_color:1, 1, 1, 1
                        font_style:'H6'
                        font_name:'font\Gotu-Regular.ttf'

                    MDTextField:
                        id: pseudo_inscri
                        width: "100dp"
                        mode: "round"
                        size_hint_x: 1.5
                        md_bg_color:(217/255,217/255,217/255,100)
                        size_hint_y: None
                        pos_hint: {"center_x": 0, "center_y": .5}



            BoxLayout:
                orientation:'horizontal'
                
                BoxLayout:
                    orientation:'horizontal'
                    
                    MDLabel:
                        text:"Prénom:"
                        size_hint_y: 1
                        halign:'center'
                        theme_text_color:"Custom"
                        text_color:1, 1, 1, 1
                        font_style:'H6'
                        font_name:'font\Gotu-Regular.ttf'
                    

                    MDTextField:
                        id: prenom_inscri
                        width: "100dp"
                        mode: "round"
                        size_hint_x: 1.5
                        md_bg_color:(217/255,217/255,217/255,100)
                        size_hint_y: None
                        pos_hint: {"center_x": 0, "center_y": .5}
                
                BoxLayout:
                    orientation:'horizontal'
                
                    MDLabel:
                        text:"Mot de passe:"
                        size_hint_y: 1
                        halign:'center'
                        theme_text_color:"Custom"
                        text_color:1, 1, 1, 1
                        font_style:'H6'
                        font_name:'font\Gotu-Regular.ttf'
                    

                    MDTextField:
                        id: mdp_inscri
                        width: "100dp"
                        mode: "round"
                        size_hint_x: 1.5
                        md_bg_color:(217/255,217/255,217/255,100)
                        size_hint_y: None
                        pos_hint: {"center_x": 0, "center_y": .5}



            BoxLayout:
                orientation:'horizontal'
                
                BoxLayout:
                    orientation:'horizontal'
                
                    MDLabel:
                        text:"Téléphone:"
                        size_hint_y: 1
                        halign:'center'
                        theme_text_color:"Custom"
                        text_color:1, 1, 1, 1
                        font_style:'H6'
                        font_name:'font\Gotu-Regular.ttf'
                    

                    MDTextField:
                        id: telephone_inscri
                        width: "100dp"
                        mode: "round"
                        size_hint_x: 1.5
                        md_bg_color:(217/255,217/255,217/255,100)
                        size_hint_y: None
                        pos_hint: {"center_x": 0, "center_y": .5}
                
                BoxLayout:
                    orientation:'horizontal'
                    
                    MDLabel:
                        text:"Confirmation:"
                        size_hint_y: 1
                        halign:'center'
                        theme_text_color:"Custom"
                        text_color:1, 1, 1, 1
                        font_style:'H6'
                        font_name:'font\Gotu-Regular.ttf'
                    

                    MDTextField:
                        id: confirmation_inscri
                        width: "100dp"
                        mode: "round"
                        size_hint_x: 1.5
                        md_bg_color:(217/255,217/255,217/255,100)
                        size_hint_y: None
                        pos_hint: {"center_x": 0, "center_y": .5}



            BoxLayout:
                orientation:'horizontal'
                
                BoxLayout:
                    orientation:'horizontal'
                    
                    MDLabel:
                        text:"Fonction:"
                        size_hint_1: 1
                        halign:'center'
                        theme_text_color:"Custom"
                        text_color:1, 1, 1, 1
                        font_style:'H6'
                        font_name:'font\Gotu-Regular.ttf'
                    

                    MDDropDownItem:
                        id:fonction_inscri
                        size_hint_x: 1.
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        text: 'Sélectionnez'
                        on_release:  app.menu_fonction.open()
                
                BoxLayout:
                    orientation:'horizontal'
                    BoxLayout:
                        orientation:'horizontal'
                        size_hint_x: .025
                    
                    MDRoundFlatIconButton:
                        text: "  Chargé-Photo  "
                        icon: "folder"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        on_release: app.file_manager_open()
                    BoxLayout:
                        orientation:'horizontal'
                        size_hint_x: .015

                    MDTextField:
                        id: photo_agent
                        pos:100,100
                        width: "100dp"
                        mode: "round"
                        size_hint_x: 0.3
                        md_bg_color:(217/255,217/255,217/255,100)
                        size_hint_y: None
                        pos_hint: {"center_x": 0.7, "center_y": .5}
                    
                    
                    



            BoxLayout:
                orientation:'horizontal'
                
                BoxLayout:
                    orientation:'horizontal'
                    
                    
                BoxLayout:
                    orientation:'horizontal'
                
                    



            BoxLayout:
                orientation:'horizontal'
                
                AnchorLayout:
                    anchor_x:'right'
                    anchor_y:'center'
                    size_hint_y: 1.9 
                    size_hint_x: 1.
                    MDRectangleFlatButton:
                        id: annuler_inscri
                        text:'    Annuler    '
                        text_color: "black"
                        theme_text_color: "Custom"
                        md_bg_color:(217/255,217/255,217/255,100)
                        size_hint_y: None
                        pos_hint: {"center_x": 2.5, "center_y": .5}
                        on_press:root.manager.current='login'
                
                AnchorLayout:
                    anchor_x:'center'
                    anchor_y:'center'
                    size_hint_y: 1.9 
                    size_hint_x: 1.
                    MagicButton:
                        id: valider_inscri
                        text: "    Enregistrer    "
                        text_color: "black"
                        on_release: self.grow(),app.enregistrer_personnel()
                        md_bg_color:(87/255,84/255,212/255,100)
                        pos_hint: {"center_x": .5, "center_y": .5}
                



            BoxLayout:
                orientation:'horizontal'
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "white"
    text_color: "black"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#4a4939"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True

#C_C
<ContentNavigationDrawerC_C>
    
    MDNavigationDrawerMenu:
        MDNavigationDrawerHeader:
            id:info_c_c
            title: "Menu"
            title_color: "black"
            text: "Alassane Konaté"
            font_name:'font\Gotu-Regular.ttf'
            #spacing: "4dp"
            padding: "12dp", "35dp", 0, "20dp"
            FitImage:
                id:infophoto_c_c
                source: "image/ID_Mahamadou.jpg"
                size_hint: 1,1.5
                radius: 50, 50, 50, 50
        MDNavigationDrawerDivider:
        #MDNavigationDrawerLabel:
            #text: "Mail"

        DrawerClickableItem:
            icon: "border-all"
            #right_text: "+99"
            text: "Tableau de bord"
            focus_color: "#e70000"
            ripple_color: "#FFF171FF"
            selected_color: "#79A825FF"
            text_color: "black"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "tableau_bord_c_c"
        MDNavigationDrawerDivider: 
        DrawerClickableItem:
            icon: "account-circle"
            text: "Client"
            text_color: "black"
            focus_color: "#e70000"
            ripple_color: "#FFF171FF"
            selected_color: "#79A825FF"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "client_c_c"
        MDNavigationDrawerDivider:
        DrawerClickableItem:
            icon: "book-open-variant"
            text: "Doléance"
            text_color: "black"
            focus_color: "#e70000"
            ripple_color: "#FFF171FF"
            selected_color: "#79A825FF"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "doleance_c_c"

 
<Content_Dialog_c_c>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDTextFieldRect:
        hint_text: "description"

    

<Content_c_c>
    orientation: "horizontal"
    size_hint_y:.5
    size_hint_x:.9 
    MDTextFieldRect:
        id:champ
        size_hint_x:.5
        mode:round
        hint_text: "description"
    BoxLayout:
        orientation:'horizontal'
        size_hint_y: 0.5
        size_hint_x:.05
    MDRaisedButton:
        id: valider_doleance
        text: "Enregistrer"
        text_color: "black"
        #padding: "12dp", "35dp", 0, "20dp"
        on_release: app.on_panel_open(self.parent.parent,self.parent)
        size_hint_y:.4
        md_bg_color:(87/255,84/255,212/255,100)
        pos_hint: {"center_x": .5, "center_y": .5}
        

            

         
<C_C>
    name:'c_c'
    BoxLayout:
        orientation:'vertical'
        
        BoxLayout:
            orientation:'horizontal'
            size_hint_y: 0.5
            height: self.minimum_height
            canvas:
                Color:
                    rgba:(255/255,181/255,0/255,100)
                Rectangle:
                    pos: self.pos
                    size: self.size

            MDIconButton:
                icon: "menu"
                pos_hint: {"center_x": .0,"center_y": .5}
                halign:'left'
                size_hint_x: 0.3
                size_hint_y: 0
                theme_text_color: "Custom"
                text_color:'white'
                on_release:nav_drawer.set_state("open")

            MDLabel:
                id:titre
                text:"DJIGUIYA  - Chargé(e) Clientèle"
                size_hint_x: 2
                halign:'left'
                pos_hint: {"center": 1}
                theme_text_color:"Custom"
                text_color:'white'
                font_style:'H3'
                font_name:'font\Gotu-Regular.ttf'
                bold: True

            MDRectangleFlatButton:
                id: deconnexion
                mode:round
                halign:"right"
                text:'Deconnecter-vous'
                text_color: "white"
                theme_text_color: "Custom"
                md_bg_color:(0/255,0/255,0/255,100)
                size_hint_y: None
                pos_hint: {"center_x": 2.5, "center_y": .5}
                on_release:root.manager.current='login'
                    
        
        BoxLayout:
            orientation:'horizontal'
            size_hint_y: 5
            height: self.minimum_height
            
                        

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager
            #SCREEN ACCEUIL
            MDScreen:
                name: "tableau_bord_c_c"
                RelativeLayout:
                    MDCard:
                        pos:50,520
                        size_hint: .2, .2
                        focus_behavior: False
                        md_bg_color: "#EC407AFF"
                        unfocus_color: "darkgrey"
                        focus_color: "grey"
                        elevation: 6
                        MDLabel:
                            text: "Clients"
                            font_style:'H5'
                            
                            text_color:"white"
                        MDLabel:
                            id:statclient
                            text: "0"
                            font_style:'H5'
                            halign: "center"
                            text_color:"white"
                    
                    MDCard:
                        pos:500,520
                        size_hint: .2, .2
                        focus_behavior: False
                        md_bg_color: "#64B5F6FF"
                        unfocus_color: "darkgrey"
                        focus_color: "grey"
                        elevation: 6
                        MDLabel:
                            text: "Nouveau Cl"
                            font_style:'H5'
                            
                            text_color:"white"
                        MDLabel:
                            id:statnew
                            text: "0"
                            font_style:'H5'
                            
                            halign: "center"
                            text_color:"white"

                   

                    MDTextField:
                        id: research_dash
                        pos:50,400
                        hint_text:"Rechercher ici"
                        icon_left:"magnify"
                        theme_text_color:"Custom"
                        size_hint: .3, .05
                        text_color:'black'
                        mode: "round"
                        bold: True
                        background_color:"white"
                        #padding_x:10
                        padding_y:5
                        on_text:
                            app.affiche_listeclient_dashboard_search()

                    MDBoxLayout:
                        orientation:'horizontal'
                        id:tableau_bord_C_C
                        pos:50,30
                    
                   

            #SCREEN GESTION DES CLIENTS
            MDScreen:
                name: "client_c_c"
                
                BoxLayout:
                    orientation:'horizontal'
                    pos:20,570
                    size_hint_y: .2
                    size_hint_x: .9
                    BoxLayout:
                        orientation:'horizontal'
                        MDLabel:
                            text:"Nom:"
                            size_hint_y: 1
                            halign:'center'
                            theme_text_color:"Custom"
                            text_color: 0, 0, 0, 1
                            font_style:'H6'
                            font_name:'font\Gotu-Regular.ttf'
                        
                        MDTextField:
                            id: nom_client
                            width: "100dp"
                            mode: "round"
                            size_hint_x: 1.5
                            md_bg_color:(217/255,217/255,217/255,100)
                            size_hint_y: None
                            pos_hint: {"center_x": 0, "center_y": .5}
                            
                    
                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .15
                        MDRaisedButton:
                            text: "Date_Naissance"
                            font_name:'font\Gotu-Regular.ttf'
                            mg_bg_color:"#F6CE67FF"
                            size_hint_y: .2
                            spacing: "10dp",0,0,0
                            pos_hint: {"center_x": 0.2, "center_y": .5}
                            on_release: app.show_date_picker_c_c()
                        
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .15
                        

                        MDTextField:
                            id: dateclient
                            width: "100dp"
                            mode: "round"
                            size_hint_x: 1
                            md_bg_color:(217/255,217/255,217/255,100)
                            size_hint_y: None
                            pos_hint: {"center_x": 0.5, "center_y": .5}
                    



                BoxLayout:
                    orientation:'horizontal'
                    pos:20,520
                    size_hint_y: .2
                    size_hint_x: .9
                    BoxLayout:
                        orientation:'horizontal'
                        MDLabel:
                            text:"Prénom:"
                            size_hint_y: 1
                            halign:'center'
                            theme_text_color:"Custom"
                            text_color:0, 0, 0, 1
                            font_style:'H6'
                            font_name:'font\Gotu-Regular.ttf'
                        

                        MDTextField:
                            id: prenom_client
                            width: "100dp"
                            mode: "round"
                            size_hint_x: 1.5
                            md_bg_color:(217/255,217/255,217/255,100)
                            size_hint_y: None
                            pos_hint: {"center_x": 0, "center_y": .5}
                    
                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .2
                        
                        MDRoundFlatIconButton:
                            text: "  Chargé-Photo  "
                            icon: "folder"
                            pos_hint: {"center_x": .5, "center_y": .5}
                            on_release: app.file_manager_open()
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .2
                        

                        MDTextField:
                            id: photo_client
                            width: "100dp"
                            mode: "round"
                            size_hint_x: 1.5
                            md_bg_color:(217/255,217/255,217/255,100)
                            size_hint_y: None
                            pos_hint: {"center_x": 0, "center_y": .5}
                        

                BoxLayout:
                    orientation:'horizontal'
                    pos:20,470
                    size_hint_y: .2
                    size_hint_x: .9
                    BoxLayout:
                        orientation:'horizontal'
                        MDLabel:
                            text:"Téléphone:"
                            size_hint_y: 1
                            halign:'center'
                            theme_text_color:"Custom"
                            text_color:0, 0, 0, 1
                            font_style:'H6'
                            font_name:'font\Gotu-Regular.ttf'
                        

                        MDTextField:
                            id: telephone_client
                            width: "100dp"
                            mode: "round"
                            size_hint_x: 1.5
                            md_bg_color:(217/255,217/255,217/255,100)
                            size_hint_y: None
                            pos_hint: {"center_x": 0, "center_y": .5}
                    
                    BoxLayout:
                        orientation:'horizontal'
                        MDLabel:
                            text:"Sexe:"
                            size_hint_y: 1
                            halign:'center'
                            theme_text_color:"Custom"
                            text_color:0, 0, 0, 1
                            font_style:'H6'
                            font_name:'font\Gotu-Regular.ttf'

                        MDDropDownItem:
                            id:sexe_client
                            size_hint_x: 1.
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            text: 'Sélectionnez'
                            on_release:  app.menu_sexe.open()
                        

                BoxLayout:
                    orientation:'horizontal'
                    pos:20,420
                    size_hint_y: .2
                    size_hint_x: .9
                    BoxLayout:
                        orientation:'horizontal'
                        
                        MDLabel:
                            text:"Adresse:"
                            size_hint_1: 1
                            halign:'center'
                            theme_text_color:"Custom"
                            text_color:0, 0, 0, 1
                            font_style:'H6'
                            font_name:'font\Gotu-Regular.ttf'
                        

                        MDTextField:
                            id: adresse_client
                            width: "100dp"
                            mode: "round"
                            size_hint_x: 1.5
                            md_bg_color:(217/255,217/255,217/255,100)
                            size_hint_y: None
                            pos_hint: {"center_x": 0, "center_y": .5}
                    
                    BoxLayout:
                        orientation:'horizontal'
                        MDLabel:
                            text:"Situation_matrimoniale:"
                            size_hint_y: 1
                            halign:'center'
                            theme_text_color:"Custom"
                            text_color:0, 0, 0, 1
                            font_style:'H6'
                            font_name:'font\Gotu-Regular.ttf'
                    
                        MDDropDownItem:
                            id:situa_matri_client
                            size_hint_x: 1.
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            text: 'Sélectionnez'
                            on_release:  app.menu_situa.open()
                        
                             
                BoxLayout:
                    orientation:'horizontal'
                    pos:20,370
                    size_hint_y: .2
                    size_hint_x: .9
                    BoxLayout:
                        orientation:'horizontal'
                        MDLabel:
                            text:"Activité:"
                            size_hint_1: 1
                            halign:'center'
                            theme_text_color:"Custom"
                            text_color:0, 0, 0, 1
                            font_style:'H6'
                            font_name:'font\Gotu-Regular.ttf'
                        

                        MDTextField:
                            id: activite_client
                            width: "100dp"
                            mode: "round"
                            size_hint_x: 1.5
                            md_bg_color:(217/255,217/255,217/255,100)
                            size_hint_y: None
                            pos_hint: {"center_x": 0, "center_y": .5}
                        
                        
                    BoxLayout:
                        orientation:'horizontal'
                        MDLabel:
                            text:"Piéce_Identité:"
                            size_hint_y: 1
                            halign:'center'
                            theme_text_color:"Custom"
                            text_color:0, 0, 0, 1
                            font_style:'H6'
                            font_name:'font\Gotu-Regular.ttf'
                        

                        MDDropDownItem:
                            id:piece_client
                            size_hint_x: 1.
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            text: 'Sélectionnez'
                            on_release:  app.menu_piece.open()
                

                BoxLayout:
                    orientation:'horizontal'
                    pos:50,370
                    size_hint_y: .05
                    size_hint_x: .9
                    canvas:
                        Color:
                            rgba:(233/255,241/255,247/255,100)
                        Rectangle:
                            pos: self.pos
                            size: self.size

                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .1
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .1
                        MagicButton:
                            id: enregistrer_client
                            text: "    Enregistrer    "
                            mode: "round"
                            text_color: "black"
                            size_hint_y:self.size_hint_y
                            size_hint_x: .15
                            pos_hint: {"center_x": 0.2, "center_y": .5}
                            on_release: 
                                self.grow()
                                app.enregistrer_clientnonvalide()
                            md_bg_color:(76/255,175/255,80/255,100)
                        
                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .1
                        MagicButton:
                            id: modifier_client
                            text: "    Modifier    "
                            mode: "round"
                            size_hint_y: self.size_hint_y
                            size_hint_x: .15
                            pos_hint: {"center_x": 0.2, "center_y": .5}
                            text_color: "black"
                            on_release: 
                                self.grow()
                                app.modifier_clientnonvalide()
                                
                            md_bg_color:(87/255,84/255,212/255,100)

                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .1
                     
                BoxLayout:
                    orientation:'horizontal'
                    pos:50,330
                    size_hint_y: .2
                    size_hint_x: .9  
                    BoxLayout:
                        orientation:'horizontal'  
                        MDTextField:
                            id: research_client_cc
                            hint_text:"Rechercher ici"
                            icon_left:"account-search"
                            theme_text_color:"Custom"
                            text_color:'black'
                            size_hint_x: 1.5
                            mode: "round"
                            bold: True
                            background_color:"white"
                            on_text:
                                app.affiche_listeclientnonvalide_search()
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .1
                    BoxLayout:
                        orientation:'horizontal'  


                BoxLayout:
                    orientation:'horizontal'
                    
                    MDBoxLayout:
                        orientation:'horizontal'
                        id:liste_client_tab
                        pos:10,20


            #SCREEN DOLEANCE
            MDScreen:
                name: "doleance_c_c"
                BoxLayout:
                    orientation:'horizontal'
                    pos:15,10
                    size_hint_y: 1.5
                    size_hint_x: 1 
                    BoxLayout:
                        orientation:'vertical' 
                        BoxLayout:
                            orientation:'horizontal'
                            MDLabel:
                                text:"Clients"
                                size_hint_y: 0.2
                                size_hint_x: 0.2
                                halign:'left'
                                theme_text_color:"Custom"
                                text_color:0, 0, 0, 1
                                font_style:'H5'
                                font_name:'font\Gotu-Regular.ttf'
                            BoxLayout:
                                orientation:'horizontal'
                                size_hint_x: 0.7
                                MDTextField:
                                    id: research_client
                                    hint_text:"Rechercher ici"
                                    icon_left:"account-search"
                                    theme_text_color:"Custom"
                                    text_color:'black'
                                    size_hint_x: .5
                                    pos_hint: {"center_x": 0, "center_y": .1}
                                    mode: "round"
                                    bold: True
                                    background_color:"white"
                                    #on_text:
                                        #app.rechercher_personne()
                                BoxLayout:
                                    orientation:'horizontal'
                        MDScrollView:

                            MDGridLayout:
                                id: box
                                cols: 1
                                adaptive_height: True
                        
                        

                
                        

                
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
            md_bg_color:(255/255,255/255,255/255,100)
            ContentNavigationDrawerC_C:
                id:content_drawer_c_c
                orientation:'vertical'
                screen_manager: screen_manager
                nav_drawer: nav_drawer

#C_A
<ContentNavigationDrawerC_A>
    MDNavigationDrawerMenu:
        MDNavigationDrawerHeader:
            id:info_c_a
            title: "Menu"
            title_color: "black"
            text: "Alassane Konaté"
            font_name:'font\Gotu-Regular.ttf'
            #spacing: "4dp"
            padding: "12dp", "35dp", 0, "20dp"
            FitImage:
                id:infophoto_c_a
                source: "image/ID_Mahamadou.jpg"
                size_hint: 1,1.5
                radius: 50, 50, 50, 50
        MDNavigationDrawerDivider:
        #MDNavigationDrawerLabel:
            #text: "Mail"

        DrawerClickableItem:
            icon: "border-all"
            #right_text: "+99"
            text: "Tableau de bord"
            text_color: "black"
            focus_color: "#e70000"
            ripple_color: "#FFF171FF"
            selected_color: "#79A825FF"
            on_press:
                root.nav_drawer_c_a.set_state("close")
                root.screen_manager_c_a.current = "tableau_bord_c_a"
        MDNavigationDrawerDivider: 
        DrawerClickableItem:
            icon: "account-circle"
            text: "Client"
            text_color: "black"
            focus_color: "#e70000"
            ripple_color: "#FFF171FF"
            selected_color: "#79A825FF"
            on_press:
                root.nav_drawer_c_a.set_state("close")
                root.screen_manager_c_a.current = "client_c_a"
        MDNavigationDrawerDivider:
        DrawerClickableItem:
            icon: "cash-multiple"
            text: "Crédit"
            text_color: "black"
            focus_color: "#e70000"
            ripple_color: "#FFF171FF"
            selected_color: "#79A825FF"
            on_press:
                root.nav_drawer_c_a.set_state("close")
                root.screen_manager_c_a.current = "credit_c_a"
        MDNavigationDrawerDivider:
        DrawerClickableItem:
            icon: "file-cabinet"
            text: "Mon portefeuille"
            text_color: "black"
            focus_color: "#e70000"
            ripple_color: "#FFF171FF"
            selected_color: "#79A825FF"
            on_press:
                root.nav_drawer_c_a.set_state("close")
                root.screen_manager_c_a.current = "portefeuille_c_a"



<Check@MDCheckBox>
    

<ListItemWithCheckbox>
    on_release:
        root.set_icon(check)
    CheckboxLeftWidget:
        id:check
        group:'check'
<C_A>
    name:'c_a'
    BoxLayout:
        orientation:'vertical'
        
        BoxLayout:
            orientation:'horizontal'
            size_hint_y: 0.5
            height: self.minimum_height
            canvas:
                Color:
                    rgba:(255/255,181/255,0/255,100)
                Rectangle:
                    pos: self.pos
                    size: self.size

            MDIconButton:
                icon: "menu"
                pos_hint: {"center_x": .0,"center_y": .5}
                halign:'left'
                size_hint_x: 0.3
                size_hint_y: 0
                theme_text_color: "Custom"
                text_color:'white'
                on_release:nav_drawer_c_a.set_state("open")

            MDLabel:
                id:titre
                text:"DJIGUIYA  - Chargé(e) D'Affaire"
                size_hint_x: 2
                halign:'left'
                pos_hint: {"center": 1}
                theme_text_color:"Custom"
                text_color:'white'
                font_style:'H3'
                font_name:'font\Gotu-Regular.ttf'
                bold: True

            MDRectangleFlatButton:
                id: deconnexion
                mode:round
                halign:"right"
                text:'Deconnecter-vous'
                text_color: "white"
                theme_text_color: "Custom"
                md_bg_color:(0/255,0/255,0/255,100)
                size_hint_y: None
                pos_hint: {"center_x": 2.5, "center_y": .5}
                on_release:root.manager.current='login'
                    
        
        BoxLayout:
            orientation:'horizontal'
            size_hint_y: 5
            height: self.minimum_height

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager_c_a
            #SCREEN ACCEUIL
            MDScreen:
                name: "tableau_bord_c_a"
                RelativeLayout:
                    MDCard:
                        pos:50,520
                        size_hint: .2, .2
                        focus_behavior: False
                        md_bg_color: "#EC407AFF"
                        unfocus_color: "darkgrey"
                        focus_color: "grey"
                        elevation: 6
                        MDLabel:
                            text: "Clients"
                            font_style:'H5'
                            
                            text_color:"white"
                        MDLabel:
                            id:statclient
                            text: "0"
                            font_style:'H5'
                            
                            halign: "center"
                            text_color:"white"
                    
                    MDCard:
                        pos:500,520
                        size_hint: .2, .2
                        focus_behavior: False
                        md_bg_color: "#64B5F6FF"
                        unfocus_color: "darkgrey"
                        focus_color: "grey"
                        elevation: 6
                        MDLabel:
                            text: "Total Crédit"
                            font_style:'H5'
                            
                            text_color:"white"
                        MDLabel:
                            id:statcacr
                            text: "0"
                            font_style:'H5'
                            
                            halign: "center"
                            text_color:"white"

                    MDCard:
                        pos:950,520
                        size_hint: .2, .2
                        focus_behavior: False
                        md_bg_color: "#76FF03FF"
                        unfocus_color: "darkgrey"
                        focus_color: "grey"
                        elevation: 6
                        MDLabel:
                            text: "Montant Crédit"
                            font_style:'H5'
                            
                            text_color:"white"
                        MDLabel:
                            id:montcacr
                            text: "0"
                            font_style:'H5'
                            
                            halign: "center"
                            text_color:"white"

                    MDCard:
                        pos:50,350
                        size_hint: .2, .2
                        focus_behavior: False
                        md_bg_color: "#FFFF00FF"
                        unfocus_color: "darkgrey"
                        focus_color: "grey"
                        elevation: 6
                        MDLabel:
                            text: "Nouveau Cl"
                            font_style:'H5'
                            
                            text_color:"white"
                        MDLabel:
                            id:statnewcacl
                            text: "0"
                            font_style:'H5'
                            
                            halign: "center"
                            text_color:"white"

                    MDCard:
                        pos:500,350
                        size_hint: .2, .2
                        focus_behavior: False
                        md_bg_color: "#8E24AAFF"
                        unfocus_color: "darkgrey"
                        focus_color: "grey"
                        elevation: 6
                        MDLabel:
                            text: "Montant payé"
                            font_style:'H5'
                            
                            text_color:"white"
                        MDLabel:
                            id:statmontpaye
                            text: "0"
                            font_style:'H5'
                            
                            halign: "center"
                            text_color:"white"


                    MDTextField:
                        id: research
                        pos:50,300
                        hint_text:"Rechercher ici"
                        icon_left:"magnify"
                        theme_text_color:"Custom"
                        size_hint: .3, .05
                        text_color:'black'
                        mode: "round"
                        bold: True
                        background_color:"white"
                        #padding_x:10
                        padding_y:5
                        #on_text:
                            #app.rechercher_personne()

                    MDBoxLayout:
                        orientation:'horizontal'
                        id:tableau_bord_C_A
                        pos:50,30

            MDScreen:
                name: "client_c_a"
                RelativeLayout:
                    MDTextField:
                        id: research
                        pos:50,500
                        hint_text:"Rechercher ici"
                        icon_left:"magnify"
                        theme_text_color:"Custom"
                        size_hint: .3, .05
                        text_color:'black'
                        mode: "round"
                        bold: True
                        background_color:"white"
                        #padding_x:10
                        padding_y:5
                        #on_text:
                            #app.rechercher_personne()

                    MDBoxLayout:
                        orientation:'horizontal'
                        id:liste
                        pos:50,30
            MDScreen:
                name: "credit_c_a"
                BoxLayout:
                    orientation:'horizontal'
                    pos:20,570
                    size_hint_y: .2
                    size_hint_x: .9
                    BoxLayout:
                        orientation:'horizontal'
                        MDLabel:
                            text:"Montant Crédit:"
                            size_hint_y: 1
                            halign:'center'
                            theme_text_color:"Custom"
                            text_color: 0, 0, 0, 1
                            font_style:'H6'
                            font_name:'font\Gotu-Regular.ttf'
                        
                        MDTextField:
                            id: montant_credit_c_a
                            width: "100dp"
                            mode: "round"
                            size_hint_x: 1.5
                            md_bg_color:(217/255,217/255,217/255,100)
                            size_hint_y: None
                            pos_hint: {"center_x": 0, "center_y": .5}
                            
                    
                    BoxLayout:
                        orientation:'horizontal'
                        
                        
                        
                    



                BoxLayout:
                    orientation:'horizontal'
                    pos:20,520
                    size_hint_y: .2
                    size_hint_x: .9
                    BoxLayout:
                        orientation:'horizontal'
                        MDLabel:
                            text:"Période_paiement:"
                            size_hint_y: 1
                            halign:'center'
                            theme_text_color:"Custom"
                            text_color:0, 0, 0, 1
                            font_style:'H6'
                            font_name:'font\Gotu-Regular.ttf'
                        

                        MDTextField:
                            id: periode
                            width: "100dp"
                            mode: "round"
                            hint_text:"en jour"
                            size_hint_x: 1.5
                            md_bg_color:(217/255,217/255,217/255,100)
                            size_hint_y: None
                            pos_hint: {"center_x": 0, "center_y": .5}
                    
                    BoxLayout:
                        orientation:'horizontal'
                        
                BoxLayout:
                    orientation:'horizontal'
                    pos:20,470
                    size_hint_y: .2
                    size_hint_x: .9
                    BoxLayout:
                        orientation:'horizontal'
                        
                        MDLabel:
                            text:"Paiement (tranche):"
                            size_hint_1: 1
                            halign:'center'
                            theme_text_color:"Custom"
                            text_color:0, 0, 0, 1
                            font_style:'H6'
                            font_name:'font\Gotu-Regular.ttf'
                        

                        MDTextField:
                            id: montant
                            width: "100dp"
                            mode: "round"
                            size_hint_x: 1.5
                            md_bg_color:(217/255,217/255,217/255,100)
                            size_hint_y: None
                            pos_hint: {"center_x": 0, "center_y": .5}
                    
                    BoxLayout:
                        orientation:'horizontal'
                    
                        

                BoxLayout:
                    orientation:'horizontal'
                    pos:20,420
                    size_hint_y: .2
                    size_hint_x: .9
                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .15
                        MDRaisedButton:
                            text: "Date_Echéance"
                            font_name:'font\Gotu-Regular.ttf'
                            mg_bg_color:"#F6CE67FF"
                            size_hint_y: .2
                            spacing: "10dp",0,0,0
                            pos_hint: {"center_x": 0.2, "center_y": .5}
                            on_release: app.show_date_picker_c_c()
                        
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .15
                        

                        MDTextField:
                            id: datecrd
                            width: "100dp"
                            mode: "round"
                            size_hint_x: 1
                            md_bg_color:(217/255,217/255,217/255,100)
                            size_hint_y: None
                            pos_hint: {"center_x": 0.5, "center_y": .5}
                    
                    BoxLayout:
                        orientation:'horizontal'
                    
                        
                        
                             
                BoxLayout:
                    orientation:'horizontal'
                    pos:20,370
                    size_hint_y: .2
                    size_hint_x: .9
                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .15
                        MDRaisedButton:
                            id:crdtcl
                            text:"Sélectionner-client"
                            size_hint_y: .2
                            spacing: "10dp",0,0,0
                            pos_hint: {"center_x": 0.2, "center_y": .5}
                            on_release:app.show_confirmation_dialog1()
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .15
                        MDLabel:
                            text:"aucun client n'est selectionné"
                            id:valeurcrdtcl
                            halign:'center'
                            theme_text_color:"Custom"
                            text_color: 0, 0, 0, 1
                            font_style:'H6'
                            font_name:'font\Gotu-Regular.ttf'
                        
                    BoxLayout:
                        orientation:'horizontal'
                        
                

                BoxLayout:
                    orientation:'horizontal'
                    pos:50,370
                    size_hint_y: .05
                    size_hint_x: .9
                    canvas:
                        Color:
                            rgba:(233/255,241/255,247/255,100)
                        Rectangle:
                            pos: self.pos
                            size: self.size

                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .1
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .1
                        MagicButton:
                            id: enregistrer_credit
                            text: "    Enregistrer    "
                            mode: "round"
                            text_color: "black"
                            size_hint_y:self.size_hint_y
                            size_hint_x: .15
                            pos_hint: {"center_x": 0.2, "center_y": .5}
                            on_release: 
                                self.grow()
                                app.enregistre_liste_credit()
                            md_bg_color:(76/255,175/255,80/255,100)
                        
                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .1
                        MagicButton:
                            id: modifier_credit
                            text: "    Modifier    "
                            mode: "round"
                            size_hint_y: self.size_hint_y
                            size_hint_x: .15
                            pos_hint: {"center_x": 0.2, "center_y": .5}
                            text_color: "black"
                            on_release: 
                                self.grow()
                                app.modifier_liste_credit()
                            md_bg_color:(87/255,84/255,212/255,100)

                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .1
                     
                BoxLayout:
                    orientation:'horizontal'
                    pos:50,330
                    size_hint_y: .2
                    size_hint_x: .9  
                    BoxLayout:
                        orientation:'horizontal'  
                        MDTextField:
                            id: research_credit
                            hint_text:"Rechercher ici"
                            icon_left:"account-search"
                            theme_text_color:"Custom"
                            text_color:'black'
                            size_hint_x: 1.5
                            mode: "round"
                            bold: True
                            background_color:"white"
                            #on_text:
                                #app.rechercher_personne()
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_x: .1
                    BoxLayout:
                        orientation:'horizontal'  


                BoxLayout:
                    orientation:'horizontal'
                    
                    MDBoxLayout:
                        orientation:'horizontal'
                        id:liste_credit_tab
                        pos:10,20
                        
            MDScreen:
                name: "portefeuille_c_a"
                FitImage:
                    id:agent
                    source: "image/ID_Mahamadou.jpg"
                    size_hint: .1,.2
                    pos:560,500
                    radius: 50, 50, 50, 50
                BoxLayout:
                    orientation:'vertical'
                    pos:50,130
                    size_hint_y: .5
                    size_hint_x: .9
                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'horizontal' 
                            BoxLayout:
                                orientation:'horizontal'  
                            MDLabel:
                                text: "N° Agent:"
                                font_style:'H5'
                                font_name:'font\Gotu-Regular.ttf'
                                
                                
                            
                        BoxLayout:
                            orientation:'horizontal' 
                            MDLabel:
                                id:numagent
                                text: "0000"
                                halign:"center"
                                font_style:'H5'
                                font_name:'font\Gotu-Regular.ttf' 
                        
                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'horizontal'
                            BoxLayout:
                                orientation:'horizontal'  
                            MDLabel:
                                text: "Nom:"
                                font_style:'H5'
                                font_name:'font\Gotu-Regular.ttf'
                                
                                
                            
                        BoxLayout:
                            orientation:'horizontal'  
                            MDLabel:
                                id:nomagent
                                text: "Aaaaaa"
                                halign:"center"
                                font_style:'H5'
                                font_name:'font\Gotu-Regular.ttf'      
                
                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'horizontal'
                            BoxLayout:
                                orientation:'horizontal'  
                            MDLabel:
                                text: "Prénom:"
                                font_style:'H5'
                                font_name:'font\Gotu-Regular.ttf'
                                
                                
                            
                        BoxLayout:
                            orientation:'horizontal'
                            MDLabel:
                                id:prenomagent
                                text: "Bbbbbb"
                                halign:"center"
                                font_style:'H5'
                                font_name:'font\Gotu-Regular.ttf'
                    
                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'horizontal' 
                            BoxLayout:
                                orientation:'horizontal' 
                            MDLabel:
                                text: "N° Portefeuille:"
                                font_style:'H5'
                                font_name:'font\Gotu-Regular.ttf'
                                
                                
                            
                        BoxLayout:
                            orientation:'horizontal'
                            MDLabel:
                                id:numportefeuille
                                text: "0000"
                                halign:"center"
                                font_style:'H5'
                                font_name:'font\Gotu-Regular.ttf'

                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'horizontal' 
                            BoxLayout:
                                orientation:'horizontal' 
                            MDLabel:
                                text: "Nombre Crédits:"
                                font_style:'H5'
                                font_name:'font\Gotu-Regular.ttf'
                                
                                
                            
                        BoxLayout:
                            orientation:'horizontal'
                            MDLabel:
                                id:nbrcdt
                                text: "0"
                                halign:"center"
                                font_style:'H5'
                                font_name:'font\Gotu-Regular.ttf'

                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'horizontal' 
                            BoxLayout:
                                orientation:'horizontal' 
                            MDLabel:
                                text: "Nombre Clients:"
                                font_style:'H5'
                                font_name:'font\Gotu-Regular.ttf'
                                
                                
                            
                        BoxLayout:
                            orientation:'horizontal'
                            MDLabel:
                                id:nbrcl
                                text: "0"
                                halign:"center"
                                font_style:'H5'
                                font_name:'font\Gotu-Regular.ttf'

                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'horizontal' 
                            BoxLayout:
                                orientation:'horizontal' 
                            MDLabel:
                                text: "Montant Financé:"
                                font_style:'H5'
                                font_name:'font\Gotu-Regular.ttf'
                                
                                
                            
                        BoxLayout:
                            orientation:'horizontal'
                            MDLabel:
                                id:montantfin
                                text: "000000"
                                font_style:'H5'
                                halign:"right"
                                font_name:'font\Gotu-Regular.ttf'
                            MDLabel:
                                halign:"center"
                                text: "Fr cfa"
                                font_style:'H5'
                                font_name:'font\Gotu-Regular.ttf'
                            BoxLayout:
                                orientation:'horizontal'


        MDNavigationDrawer:
            id: nav_drawer_c_a
            radius: (0, 16, 16, 0)
            md_bg_color:(255/255,255/255,255/255,100)
            ContentNavigationDrawerC_A:
                id:content_drawer_c_a
                orientation:'vertical'
                screen_manager_c_a: screen_manager_c_a
                nav_drawer_c_a: nav_drawer_c_a




#CAISSIER
<ListItemWithCheckbox_caissier>

    on_release:
        root.set_icon(check)
        app.get_client3(self.text,self.secondary_text)
    CheckboxLeftWidget:
        id:check
        group:'check'
    
<Content_Dialog_caissier>
    orientation: "vertical"
    #spacing: "12dp"
    size_hint_y: None
    height: "400dp"
    MDTextField:
        id: research_credit
        hint_text:"Rechercher ici"
        icon_left:"magnify"
        theme_text_color:"Custom"
        text_color:'black'
        size_hint_x: .8
        mode: "round"
        bold: True
        background_color:"white"
        on_text:
            app.recherche_dialog3(self.text,self.parent.ids.boxcldepot)
        
    MDScrollView:
        MDGridLayout:
            id: boxcldepot
            cols: 1
            adaptive_height: True
            ListItemWithCheckbox_caissier:
                id:listcheck
                

<ContentNavigationDrawer_CAISSIER>
    MDNavigationDrawerMenu:
        MDNavigationDrawerHeader:
            id:info_caissier
            title: "Menu"
            title_color: "black"
            text: "Alassane Konaté"
            font_name:'font\Gotu-Regular.ttf'
            #spacing: "4dp"
            padding: "12dp", "35dp", 0, "20dp"
            FitImage:
                id:infophoto_caissier
                source: "image/ID_Mahamadou.jpg"
                size_hint: 1,1.5
                radius: 50, 50, 50, 50
        MDNavigationDrawerDivider:
        #MDNavigationDrawerLabel:
            #text: "Mail"

        DrawerClickableItem:
            icon: "border-all"
            #right_text: "+99"
            text: "Tableau de bord"
            text_color: "black"
            focus_color: "#e70000"
            ripple_color: "#FFF171FF"
            selected_color: "#79A825FF"
            on_press:
                root.nav_drawer_caissier.set_state("close")
                root.screen_manager_caissier.current = "tableau_bord_caissier"
        MDNavigationDrawerDivider: 
        DrawerClickableItem:
            icon: "arrow-down-left"
            text: "Dépôt"
            text_color: "black"
            focus_color: "#e70000"
            ripple_color: "#FFF171FF"
            selected_color: "#79A825FF"
            on_press:
                root.nav_drawer_caissier.set_state("close")
                root.screen_manager_caissier.current = "depot_caissier"
        MDNavigationDrawerDivider:
        DrawerClickableItem:
            icon: "arrow-up-right"
            text: "Rétrait"
            text_color: "black"
            focus_color: "#e70000"
            ripple_color: "#FFF171FF"
            selected_color: "#79A825FF"
            on_press:
                root.nav_drawer_caissier.set_state("close")
                root.screen_manager_caissier.current = "retrait_caissier"
        MDNavigationDrawerDivider:
        DrawerClickableItem:
            icon: "card-text-outline"
            text: "Rapport journalier"
            text_color: "black"
            focus_color: "#e70000"
            ripple_color: "#FFF171FF"
            selected_color: "#79A825FF"
            on_press:
                root.nav_drawer_caissier.set_state("close")
                root.screen_manager_caissier.current = "rapportjournalier_caissier"

<CAISSIER>
    name:'caissier'
    BoxLayout:
        orientation:'vertical'
        
        BoxLayout:
            orientation:'horizontal'
            size_hint_y: 0.5
            height: self.minimum_height
            canvas:
                Color:
                    rgba:(255/255,181/255,0/255,100)
                Rectangle:
                    pos: self.pos
                    size: self.size

            MDIconButton:
                icon: "menu"
                pos_hint: {"center_x": .0,"center_y": .5}
                halign:'left'
                size_hint_x: 0.3
                size_hint_y: 0
                theme_text_color: "Custom"
                text_color:'white'
                on_release:nav_drawer_caissier.set_state("open")

            MDLabel:
                id:titre
                text:"DJIGUIYA  - Caissier"
                size_hint_x: 2
                halign:'left'
                pos_hint: {"center": 1}
                theme_text_color:"Custom"
                text_color:'white'
                font_style:'H3'
                font_name:'font\Gotu-Regular.ttf'
                bold: True

            MDRectangleFlatButton:
                id: deconnexion
                mode:round
                halign:"right"
                text:'Deconnecter-vous'
                text_color: "white"
                theme_text_color: "Custom"
                md_bg_color:(0/255,0/255,0/255,100)
                size_hint_y: None
                pos_hint: {"center_x": 2.5, "center_y": .5}
                on_release:root.manager.current='login'
                    
        
        BoxLayout:
            orientation:'horizontal'
            size_hint_y: 5
            height: self.minimum_height

    MDNavigationLayout:
        id:layout

        MDScreenManager:
            id: screen_manager_caissier
            #SCREEN ACCEUIL
            MDScreen:
                name: "tableau_bord_caissier"
                RelativeLayout:
                    MDCard:
                        pos:50,520
                        size_hint: .2, .2
                        focus_behavior: False
                        md_bg_color: "#2196F3FF"
                        unfocus_color: "darkgrey"
                        focus_color: "grey"
                        elevation: 6
                        MDLabel:
                            text: "Total Dépôt"
                            font_style:'H5'
                            
                            text_color:"white"
                        MDLabel:
                            id:statdepot
                            text: "0"
                            font_style:'H5'
                            
                            halign: "center"
                            text_color:"white"
                    
                    MDCard:
                        pos:500,520
                        size_hint: .2, .2
                        focus_behavior: False
                        md_bg_color: "#00E676FF"
                        unfocus_color: "darkgrey"
                        focus_color: "grey"
                        elevation: 6
                        MDLabel:
                            text: "Total Retrait"
                            font_style:'H5'
                            
                            text_color:"white"
                        MDLabel:
                            id:statretrait
                            text: "0"
                            font_style:'H5'
                            
                            halign: "center"
                            text_color:"white"

                    


                    MDTextField:
                        id: research_trans
                        pos:50,360
                        hint_text:"Rechercher ici"
                        icon_left:"magnify"
                        theme_text_color:"Custom"
                        size_hint: .3, .05
                        text_color:'black'
                        mode: "round"
                        bold: True
                        background_color:"white"
                        #padding_x:10
                        padding_y:5
                        #on_text:
                            #app.rechercher_personne()

                    MDBoxLayout:
                        orientation:'horizontal'
                        id:tableau_bord_CAISSIER
                        pos:50,30


            #SCREEN DEPOT
            MDScreen:
                name: "depot_caissier"
                BoxLayout:
                    orientation:'vertical'
                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'vertical'
                            BoxLayout:
                                orientation:'horizontal'
                            BoxLayout:
                                orientation:'horizontal'
                                BoxLayout:
                                    orientation:'horizontal'
                                    size_hint_x: .15
                                MDRaisedButton:
                                    id:cldepot
                                    text:"Sélectionner-client"
                                    size_hint_y: .4
                                    spacing: "10dp",0,0,0
                                    pos_hint: {"center_x": 0.2, "center_y": .5}
                                    on_release:app.show_confirmation_dialog3()
                                BoxLayout:
                                    orientation:'horizontal'
                                    size_hint_x: .15
                                MDLabel:
                                    text:"aucun client n'est selectionné"
                                    id:cldepot
                                    halign:'center'
                                    theme_text_color:"Custom"
                                    text_color: 0, 0, 0, 1
                                    font_style:'H6'
                                    font_name:'font\Gotu-Regular.ttf'
                                    
                                
                            BoxLayout:
                                orientation:'horizontal'
                                MDLabel:
                                    text:"Type Compte:"
                                    size_hint_y: 1
                                    halign:'center'
                                    theme_text_color:"Custom"
                                    text_color:0, 0, 0, 1
                                    font_style:'H6'
                                    font_name:'font\Gotu-Regular.ttf'
                                

                                MDDropDownItem:
                                    id:typecompte
                                    size_hint_x: 1.5
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu_comptedepot.open()
                                
                            
                            BoxLayout:
                                orientation:'horizontal'
                                MDLabel:
                                    text:"Montant:"
                                    size_hint_1: 1
                                    halign:'center'
                                    theme_text_color:"Custom"
                                    text_color:0, 0, 0, 1
                                    font_style:'H6'
                                    font_name:'font\Gotu-Regular.ttf'
                                

                                MDTextField:
                                    id: montantdepot
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 1.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                            
                                
                    
                        BoxLayout:
                            orientation:'vertical'
                            
                        

                    BoxLayout:
                        orientation:'vertical'
                        
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_y: .2
                            size_hint_x: .9
                            canvas:
                                Color:
                                    rgba:(233/255,241/255,247/255,100)
                                Rectangle:
                                    pos: self.pos
                                    size: self.size

                            BoxLayout:
                                orientation:'horizontal'
                                BoxLayout:
                                    orientation:'horizontal'
                                    size_hint_x: .1
                                BoxLayout:
                                    orientation:'horizontal'
                                    size_hint_x: .1
                                MagicButton:
                                    id: enregistrer_depot
                                    text: "    Enregistrer    "
                                    mode: "round"
                                    text_color: "black"
                                    size_hint_y:self.size_hint_y
                                    size_hint_x: .15
                                    pos_hint: {"center_x": 0.2, "center_y": .5}
                                    on_release: 
                                        self.grow()
                                        app.enregistre_depot()
                                        
                                    md_bg_color:(76/255,175/255,80/255,100)
                                
                            BoxLayout:
                                orientation:'horizontal'
                                BoxLayout:
                                    orientation:'horizontal'
                                    size_hint_x: .1
                                MagicButton:
                                    id: modifier_depot
                                    text: "    Modifier    "
                                    mode: "round"
                                    size_hint_y: self.size_hint_y
                                    size_hint_x: .15
                                    pos_hint: {"center_x": 0.2, "center_y": .5}
                                    text_color: "black"
                                    on_release: 
                                        self.grow()
                                        
                                    md_bg_color:(87/255,84/255,212/255,100)

                                BoxLayout:
                                    orientation:'horizontal'
                                    size_hint_x: .1

                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_y: .2
                            size_hint_x: .9  
                            BoxLayout:
                                orientation:'horizontal' 
                                BoxLayout:
                                    orientation:'horizontal' 
                                    size_hint_x: .2 
                                MDTextField:
                                    id: research_depot
                                    hint_text:"Rechercher ici"
                                    icon_left:"magnify"
                                    theme_text_color:"Custom"
                                    text_color:'black'
                                    size_hint_x: 1.5
                                    mode: "round"
                                    bold: True
                                    background_color:"white"
                                    #on_text:
                                        #app.rechercher_personne()
                                BoxLayout:
                                    orientation:'horizontal'
                                    size_hint_x: .1
                            BoxLayout:
                                orientation:'horizontal' 

                        BoxLayout:
                            orientation:'horizontal'
                            id:liste_depot
                            
                            
                        
                    
            #SCREEN RETRAIT
            MDScreen:
                name: "retrait_caissier"
                BoxLayout:
                    orientation:'vertical'
                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'vertical'
                            BoxLayout:
                                orientation:'horizontal'
                            BoxLayout:
                                orientation:'horizontal'
                                BoxLayout:
                                    orientation:'horizontal'
                                    size_hint_x: .15
                                MDRaisedButton:
                                    id:clretrait
                                    text:"Sélectionner-client"
                                    size_hint_y: .4
                                    spacing: "10dp",0,0,0
                                    pos_hint: {"center_x": 0.2, "center_y": .5}
                                    on_release:app.show_confirmation_dialog3()
                                BoxLayout:
                                    orientation:'horizontal'
                                    size_hint_x: .15
                                MDLabel:
                                    text:"aucun client n'est selectionné"
                                    id:clretrait
                                    halign:'center'
                                    theme_text_color:"Custom"
                                    text_color: 0, 0, 0, 1
                                    font_style:'H6'
                                    font_name:'font\Gotu-Regular.ttf'
                                    
                                

                            BoxLayout:
                                orientation:'horizontal'
                                MDLabel:
                                    text:"Type Compte:"
                                    size_hint_y: 1
                                    halign:'center'
                                    theme_text_color:"Custom"
                                    text_color:0, 0, 0, 1
                                    font_style:'H6'
                                    font_name:'font\Gotu-Regular.ttf'
                                

                                MDDropDownItem:
                                    id:typecompteretrait
                                    size_hint_x: 1.5
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu_compteretrait.open()
                                
                            
                            BoxLayout:
                                orientation:'horizontal'
                                MDLabel:
                                    text:"Montant:"
                                    size_hint_1: 1
                                    halign:'center'
                                    theme_text_color:"Custom"
                                    text_color:0, 0, 0, 1
                                    font_style:'H6'
                                    font_name:'font\Gotu-Regular.ttf'
                                

                                MDTextField:
                                    id: montantretrait
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 1.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                            
                                
                    
                        BoxLayout:
                            orientation:'vertical'
                            
                        

                    BoxLayout:
                        orientation:'vertical'
                        
                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_y: .2
                            size_hint_x: .9
                            canvas:
                                Color:
                                    rgba:(233/255,241/255,247/255,100)
                                Rectangle:
                                    pos: self.pos
                                    size: self.size

                            BoxLayout:
                                orientation:'horizontal'
                                BoxLayout:
                                    orientation:'horizontal'
                                    size_hint_x: .1
                                BoxLayout:
                                    orientation:'horizontal'
                                    size_hint_x: .1
                                MagicButton:
                                    id: enregistrer_retrait
                                    text: "    Enregistrer    "
                                    mode: "round"
                                    text_color: "black"
                                    size_hint_y:self.size_hint_y
                                    size_hint_x: .15
                                    pos_hint: {"center_x": 0.2, "center_y": .5}
                                    on_release: 
                                        self.grow()
                                        app.enregistre_retrait()
                                    md_bg_color:(76/255,175/255,80/255,100)
                                
                            BoxLayout:
                                orientation:'horizontal'
                                BoxLayout:
                                    orientation:'horizontal'
                                    size_hint_x: .1
                                MagicButton:
                                    id: modifier_retrait
                                    text: "    Modifier    "
                                    mode: "round"
                                    size_hint_y: self.size_hint_y
                                    size_hint_x: .15
                                    pos_hint: {"center_x": 0.2, "center_y": .5}
                                    text_color: "black"
                                    on_release: 
                                        self.grow()
                                        
                                    md_bg_color:(87/255,84/255,212/255,100)

                                BoxLayout:
                                    orientation:'horizontal'
                                    size_hint_x: .1

                        BoxLayout:
                            orientation:'horizontal'
                            size_hint_y: .2
                            size_hint_x: .9  
                            BoxLayout:
                                orientation:'horizontal' 
                                BoxLayout:
                                    orientation:'horizontal' 
                                    size_hint_x: .2 
                                MDTextField:
                                    id: research_retrait
                                    hint_text:"Rechercher ici"
                                    icon_left:"magnify"
                                    theme_text_color:"Custom"
                                    text_color:'black'
                                    size_hint_x: 1.5
                                    mode: "round"
                                    bold: True
                                    background_color:"white"
                                    #on_text:
                                        #app.rechercher_personne()
                                BoxLayout:
                                    orientation:'horizontal'
                                    size_hint_x: .1
                            BoxLayout:
                                orientation:'horizontal' 

                        BoxLayout:
                            orientation:'horizontal'
                            id:liste_retrait
                            
            
            #SCREEN RAPPORT
            MDScreen:
                name: "rapportjournalier_caissier"
                

        MDNavigationDrawer:
            id: nav_drawer_caissier
            radius: (0, 16, 16, 0)
            md_bg_color:(255/255,255/255,255/255,100)
            ContentNavigationDrawer_CAISSIER:
                id:content_drawer_caissier
                orientation:'vertical'
                screen_manager_caissier: screen_manager_caissier
                nav_drawer_caissier: nav_drawer_caissier


#CHEF
<ContentNavigationDrawer_CHEF>
    MDNavigationDrawerMenu:
        MDNavigationDrawerHeader:
            id:info_chef
            title: "Menu"
            title_color: "black"
            text: "Alassane Konaté"
            font_name:'font\Gotu-Regular.ttf'
            #spacing: "4dp"
            padding: "12dp", "35dp", 0, "20dp"
            FitImage:
                id:infophoto_chef
                source: "image/ID_Mahamadou.jpg"
                size_hint: 1,1.5
                radius: 50, 50, 50, 50
        MDNavigationDrawerDivider:
        #MDNavigationDrawerLabel:
            #text: "Mail"

        DrawerClickableItem:
            icon: "border-all"
            #right_text: "+99"
            text: "Tableau de bord"
            text_color: "black"
            focus_color: "#e70000"
            ripple_color: "#FFF171FF"
            selected_color: "#79A825FF"
            on_press:
                root.nav_drawer_chef.set_state("close")
                root.screen_manager_chef.current = "tableau_bord_chef"
        MDNavigationDrawerDivider: 
        DrawerClickableItem:
            icon: "account"
            text: "client"
            text_color: "black"
            focus_color: "#e70000"
            ripple_color: "#FFF171FF"
            selected_color: "#79A825FF"
            on_press:
                root.nav_drawer_chef.set_state("close")
                root.screen_manager_chef.current = "client"
        MDNavigationDrawerDivider:
        
<CHEF>
    name:'chef'
    BoxLayout:
        orientation:'vertical'
        
        BoxLayout:
            orientation:'horizontal'
            size_hint_y: 0.5
            height: self.minimum_height
            canvas:
                Color:
                    rgba:(255/255,181/255,0/255,100)
                Rectangle:
                    pos: self.pos
                    size: self.size

            MDIconButton:
                icon: "menu"
                pos_hint: {"center_x": .0,"center_y": .5}
                halign:'left'
                size_hint_x: 0.3
                size_hint_y: 0
                theme_text_color: "Custom"
                text_color:'white'
                on_release:nav_drawer_chef.set_state("open")

            MDLabel:
                id:titre
                text:"DJIGUIYA  - Chef d'agence"
                size_hint_x: 2
                halign:'left'
                pos_hint: {"center": 1}
                theme_text_color:"Custom"
                text_color:'white'
                font_style:'H3'
                font_name:'font\Gotu-Regular.ttf'
                bold: True

            MDRectangleFlatButton:
                id: deconnexion
                mode:round
                halign:"right"
                text:'Deconnecter-vous'
                text_color: "white"
                theme_text_color: "Custom"
                md_bg_color:(0/255,0/255,0/255,100)
                size_hint_y: None
                pos_hint: {"center_x": 2.5, "center_y": .5}
                on_release:root.manager.current='login'
                    
        
        BoxLayout:
            orientation:'horizontal'
            size_hint_y: 5
            height: self.minimum_height

    MDNavigationLayout:
        id:layout

        MDScreenManager:
            id: screen_manager_chef
            #SCREEN ACCEUIL
            MDScreen:
                name: "tableau_bord_chef"
            #SCREEN CLIENT
            MDScreen:
                name: "client"
                BoxLayout:
                    orientation:'vertical'
                    BoxLayout:
                        orientation:'horizontal'
                        BoxLayout:
                            orientation:'vertical'
                            BoxLayout:
                                orientation:'horizontal'
                                size_hint_y:0.6
                                BoxLayout:
                                    orientation:'horizontal'
                                    id:photo_client
                                    size_hint_x:0.25
                                    FitImage:
                                        id:photo_cl
                                        source: "image/photo.png"
                                        size_hint_y:0.70
                                        radius: 50, 50, 50, 50
                                BoxLayout:
                                    orientation:'horizontal'
                                    BoxLayout:
                                        orientation:'horizontal'
                                        size_hint_x:0.15
                                    BoxLayout:
                                        orientation:'vertical'
                                        BoxLayout:
                                            orientation:'horizontal'
                                            MDRectangleFlatButton:
                                                id: portefeuille
                                                mode:round
                                                halign:"right"
                                                text:'Portefeuille'
                                                pos_hint: {"center_x": .5, "center_y": .2}
                                                size_hint_x:0.25
                                                spacing:0,0,0,"20dp"
                                                on_release:app.show_confirmation_dialog2()
                                            MDLabel:
                                                id:choix_por
                                                text:"aucun portefeuille"
                                                halign:'center'
                                                pos_hint: {"center_x": .3, "center_y": .2}
                                                theme_text_color:"Custom"
                                                text_color:'black'
                                                font_style:'H6'
                                                font_name:'font\Gotu-Regular.ttf'
                                                bold: True
                                        MDTextFieldRect:
                                            id:descr
                                            size_hint: 0.75, None
                                            height: "100dp"
                                            background_color: app.theme_cls.bg_normal
                                BoxLayout:
                                    orientation:'horizontal'
                                    
                                        
                            BoxLayout:
                                orientation:'horizontal'
                                size_hint_y:0.3
                                
                                BoxLayout:
                                    orientation:'horizontal'
                                    size_hint_x:0.15
                                    
                                MDRectangleFlatButton:
                                    id: validerclient
                                    mode:round
                                    #halign:"right"
                                    text:'Valider'
                                    text_color:"black"
                                    bold:True
                                    pos_hint: {"center_x": .5, "center_y": .2}
                                    size_hint_x:0.25
                                    spacing:0,0,0,"20dp"
                                    md_bg_color:(0/255,200/255,83/255,100)
                                    on_release:app.enregistre_listeclientnonvalide_chef()
                                BoxLayout:
                                    orientation:'horizontal'
                                    
                            
                 
                    BoxLayout:
                        orientation:'horizontal'
                        canvas:
                            Color:
                                rgba:(87/255,84/255,212/255,100)
                            Rectangle:
                                pos: self.pos
                                size: self.size
                        #size_hint_y:2.5
                        id:datatablevalide

        MDNavigationDrawer:
            id: nav_drawer_chef
            radius: (0, 16, 16, 0)
            md_bg_color:(255/255,255/255,255/255,100)
            ContentNavigationDrawer_CHEF:
                id:content_drawer_chef
                orientation:'vertical'
                screen_manager_chef: screen_manager_chef
                nav_drawer_chef: nav_drawer_chef


MDScreen:
    name:'main'
    ScreenManager:
        id:manager
        #LE SCREEN DE LOGIN
        Login:
        #LE SCREEN D'INSCRIPTION
        Inscription:
        #LE SCREEN DU CHARGE CLIENTELE
        C_C:
        #LE SCREEN DU CHARGE D'AFFAIRE
        C_A:
        #LE SCREEN DU CAISSIER
        CAISSIER:
        #LE SCREEN DU CHEF
        CHEF:
        
"""
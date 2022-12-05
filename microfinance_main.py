from email.mime import base
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty , StringProperty,DictProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import BaseButton,MDFlatButton
from kivymd.uix.textfield import MDTextFieldRect
from kivy.core.window import Window,Config
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.list import TwoLineAvatarListItem,ThreeLineAvatarListItem,ImageRightWidget,IRightBodyTouch,ImageLeftWidget, OneLineAvatarIconListItem
from kivy.utils import get_color_from_hex
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd import images_path
from kivy.metrics import dp
import os
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
import pymysql
import shutil
from microfinance_kivy import kv
Window.fullscreen='fake'

class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''

class ListItemWithCheckbox(OneLineAvatarIconListItem):
    def set_icon(self,instance_check):
        instance_check.active=True
        #txt=instance_check.parent.text
        #sctxt=instance_check.parent.secondary_text
        #check_cl=txt+sctxt
        #print(check_cl)
        check_list=instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check !=instance_check:
                check.active=False
        
    pass
class ListItemWithCheckbox_caissier(TwoLineAvatarListItem):
    def set_icon(self,instance_check):
        instance_check.active=True
        check_list=instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check !=instance_check:
                check.active=False
    pass
class Content_Dialog_c_c(MDBoxLayout):
    pass
class Content_Dialog_caissier(MDBoxLayout):
    pass
class Content_c_c(MDBoxLayout):
     pass
class ContentNavigationDrawer_CHEF(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    pass
class ContentNavigationDrawer_CAISSIER(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    pass

class ContentNavigationDrawerC_C(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    pass
class ContentNavigationDrawerC_A(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    pass
class mana(MDScreenManager):
     pass
class CHEF(MDScreen):
     pass
class CAISSIER(MDScreen):
     pass

class C_C(MDScreen):
     pass

class C_A(MDScreen):
     pass
class Inscription(MDScreen):
     
     pass

class Login(MDScreen):
     pass

class base_de_donnees:
    def __init__(self) -> None:
        self.con=pymysql.connect(host="localhost",user="root",password="",database="microfinance")
        self.cur=self.con.cursor()
        '''cur=conn.cursor()
        cur.execute("select num_chambre,categorie from chambre;")
        l=[]
        output=cur.fetchall()
        for i in output:
        a=str(i[0])+" "+i[1]
        l.append(a)
        conn.close()
        return l
        try:
        if prix=="":
            messagebox.showwarning("Attention","Veuillez donner le prix ")
        else:
         conn=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
         cur=conn.cursor()
         cur.execute("insert into reservation_chambre (num_chambre,nom_client,prenom_client,telephone,date_reservation,prix) values (%s,%s,%s,%s,%s,%s);",(num_chambre,client_nom,client_prenom,client_telephone,date,prix))
         conn.commit()
         messagebox.showinfo("Success","Chambre reservé")
         afficher()

        except Exception as e:
        messagebox.showerror("Echec",e)
        conn.rollback()
        conn.close()'''
    def liste_clientnonvalide_search(self,text):
        try:
            self.cur.execute("select idclient,nom,prenom,telephone,adresse,activite,sexe,date_naissance,situation_matri,piece_identite from clientnonvalide where nom like'%"+text+"%' or prenom like'%"+text+"%' or telephone like'%"+text+"%'  ")
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)
    def dashboard_c_c_search(self,text):
        try:
            self.cur.execute("select c.idclient,c.nom,c.prenom,c.telephone,c.adresse,c.situation_matri,c.date_naissance,c.piece_identite,cc.solde,co.solde,ce.solde,c.portefeuille,pe.id_personnel,pe.prenom,pe.nom,c.date_creation from client c,compte_credit cc,compte_courant co,compte_epargne ce,personnel pe,portefeuille po where ((c.idclient=cc.client and c.idclient=co.client and c.idclient=ce.client) and ((c.portefeuille=po.id_portefeuille) and po.personnel=pe.id_personnel)) and c.nom like'%"+text+"%' or c.prenom like'%"+text+"%' or c.telephone like'%"+text+"%' ")
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)
    def liste_transaction(self,agent):
        try:
            self.cur.execute("select tr.id_transaction, cl.nom,cl.prenom,cl.telephone,tr.type_transaction,tr.montant,tr.type_compte,tr.date_transaction from transaction tr,client cl where tr.client=cl.idclient  and tr.personnel=%s",(agent))
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)
    def nbrretrait(self,agent):
        try:
            self.cur.execute("select count(id_transaction) from transaction where (personnel=%s and type_transaction='retrait') and date_transaction=current_date ",(agent))
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    def nbrdepot(self,agent):
        try:
            self.cur.execute("select count(id_transaction) from transaction where (personnel=%s and type_transaction='dépôt') and date_transaction=current_date ",(agent))
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    def liste_retrait(self):
        try:
            self.cur.execute("select tr.id_transaction, cl.nom,cl.prenom,cl.telephone,tr.type_transaction,tr.montant,tr.type_compte,tr.date_transaction from transaction tr,client cl where tr.client=cl.idclient and tr.type_transaction='retrait'")
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)
    def updatecompte_epargne_retrait(self,montant,id_cj):
        try:
            self.cur.execute("update compte_epargne set solde=solde-%s where client=%s",(montant,id_cj))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return e
    def verifier_compte_epargne(self,client):
        try:
            self.cur.execute("select solde from compte_epargne where client=%s ",(client))
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    def verifier_compte_credit(self,client):
        try:
            self.cur.execute("select solde from compte_credit where client=%s ",(client))
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    def updatecompte_credit_retrait(self,montant,id_cj):
        try:
            self.cur.execute("update compte_credit set solde=solde-%s where client=%s",(montant,id_cj))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return e
    def updatecompte_epargne(self,montant,id_cj):
        try:
            self.cur.execute("update compte_epargne set solde=solde+%s where client=%s",(montant,id_cj))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return e
    def updatecompte_courant(self,montant,id_cj):
        try:
            self.cur.execute("update compte_courant set solde=solde+%s where client=%s",(montant,id_cj))
            self.cur.execute("update credit set montant_reste=montant_reste-%s where etat='En cours' and client=%s ",(montant,id_cj))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return e
    def enregistrer_transaction(self,client,type_compte,type_trans,montant,agent):
        try:
            self.cur.execute("insert into transaction(client,type_compte,type_transaction,montant,personnel) values (%s,%s,%s,%s,%s)",(client,type_compte,type_trans,montant,agent))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return e
    def liste_depot(self):
        try:
            self.cur.execute("select tr.id_transaction, cl.nom,cl.prenom,cl.telephone,tr.type_transaction,tr.montant,tr.type_compte,tr.date_transaction from transaction tr,client cl where tr.client=cl.idclient and tr.type_transaction='dépôt'")
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)
    def client_caissier_recherche(self,text):
        try:
            self.cur.execute("select idclient,nom,prenom,telephone,photo from client where nom like '%"+text+"%' or prenom like '%"+text+"%' or telephone like '%"+text+"%' ")
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)
    def client_caissier(self):
        try:
            self.cur.execute("select idclient,nom,prenom,telephone,photo from client ")
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)
    def clients_dash_c_a(self,id_ca):
        try:
            self.cur.execute("select cr.id_credit,cl.nom,cl.prenom,cl.telephone,cr.montant_credit,cr.montant_paye,cr.montant_reste,cr.date_echeance from client cl,portefeuille po,credit cr where (cl.portefeuille=po.id_portefeuille and po.personnel=%s) and (cl.portefeuille=cr.portefeuille and cr.client=cl.idclient) ",id_ca)
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)
    def updatecompte_update_credit(self,montant,id_cj):
        try:
            self.cur.execute("update compte_credit set solde=%s where client=%s",(montant,id_cj))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return e
    def update_credit(self,montant_cr,periode,montant_rem,date_eche_,id_cr,client):
        try:
            self.cur.execute("update credit set montant_credit=%s,montant_reste=%s,periode_remboursement=%s,montant_remboursement=%s,date_echeance=%s,client=%s where id_credit=%s",(montant_cr,montant_cr,periode,montant_rem,date_eche_,client,id_cr))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return e
    def tel_cl(self,tel_cl):
        try:
            self.cur.execute("select idclient from client where telephone='"+tel_cl+"'")
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    def updatecompte_credit(self,montant,id_cj):
        try:
            self.cur.execute("update compte_credit set solde=solde+%s where client=%s",(montant,id_cj))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return e
    def info_c_a(self,id_ca):
        try:
            self.cur.execute("select id_personnel,nom,prenom,id_portefeuille from personnel ,portefeuille where id_personnel="+id_ca+"")
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    def enregistrer_credit(self,montant_credit,periode_rembrs,montant_rembs,date_eche,client,portefeuile,personnel):
        try:
            self.cur.execute("insert into credit(montant_credit,montant_paye,montant_reste,periode_remboursement,montant_remboursement,date_echeance,etat,client,portefeuille,personnel) values (%s,0,%s,%s,%s,%s,'En cours',%s,%s,%s)",(montant_credit,montant_credit,periode_rembrs,montant_rembs,date_eche,client,portefeuile,personnel ))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return e
    def liste_credits(self,id_ca):
        try:
            self.cur.execute("select cr.id_credit,cr.montant_credit,cr.montant_paye,cr.montant_reste,cr.date_approbation,cr.date_echeance,cr.periode_remboursement,cr.montant_remboursement,cl.prenom,cl.nom,cl.telephone,cr.etat from credit cr,client cl where (cl.idclient=cr.client and cr.portefeuille=cl.portefeuille) and cr.personnel="+id_ca+" ")
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)
    def client_c_a(self,id_ca):
        try:
            self.cur.execute("select cl.idclient,cl.nom,cl.prenom,cl.telephone from client cl,portefeuille po where cl.portefeuille=po.id_portefeuille and po.personnel="+id_ca+" ")
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)
    def clients_c_a(self,id_ca):
        try:
            self.cur.execute("select cl.idclient,cl.nom,cl.prenom,cl.telephone,cl.adresse,cl.activite,cl.date_creation from client cl,portefeuille po where cl.portefeuille=po.id_portefeuille and po.personnel=%s ;",id_ca)
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)
    def sommecreditpaye_c_a(self,id_ca):
        try:
            self.cur.execute("select sum(montant_paye) from credit  where personnel="+id_ca+" ")
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    def nbrclientnew_c_a(self,id_ca):
        try:
            self.cur.execute("select count(cl.idclient) from client cl,portefeuille po where (cl.portefeuille=po.id_portefeuille and po.personnel="+id_ca+") and cl.date_creation=current_date ")
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    def sommecredit_c_a(self,id_ca):
        try:
            self.cur.execute("select sum(montant_credit) from credit  where personnel="+id_ca+" ")
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    def nbrcredit_c_a(self,id_ca):
        try:
            self.cur.execute("select count(id_credit) from credit  where personnel="+id_ca+" ")
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    def nbrclient_c_a(self,id_ca):
        try:
            self.cur.execute("select count(cl.idclient) from client cl,portefeuille po where cl.portefeuille=po.id_portefeuille and po.personnel="+id_ca+" ")
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    def enregistrecompteepargne(self,client):
        try:
            self.cur.execute("insert into compte_epargne(solde,client) values (0,%s)",(client))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return 0
    def enregistrecomptecredit(self,client):
        try:
            self.cur.execute("insert into compte_credit(solde,client) values (0,%s)",(client))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return 0
    def enregistrecomptecourant(self,client):
        try:
            self.cur.execute("insert into compte_courant(solde,client) values (0,%s)",(client))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return 0
    def idclient(self,telephone):
        try:
            self.cur.execute("select idclient from client where telephone ='"+telephone+"'")
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    def enregistrer_client(self,nom,prenom,telephone,adresse,activite,date_nai,photo,sexe,situa_matri,piece,portefeuille):
        try:
            self.cur.execute("insert into client(nom,prenom,telephone,adresse,activite,date_naissance,photo,sexe,situation_matri,piece_identite,portefeuille) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(nom,prenom,telephone,adresse,activite,date_nai,photo,sexe,situa_matri,piece,portefeuille))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return e
    def liste_clientnonvalide_doleance(self):
        try:
            self.cur.execute("select idclient,nom,prenom,telephone,adresse,activite,sexe,date_naissance,situation_matri,piece_identite from clientnonvalide,doleance where idclient=clientnonvalide and telephone not in(select telephone from client) ")
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)
    def liste_clientnonvalide_dol(self,id):
        try:
            self.cur.execute("select photo,description from clientnonvalide,doleance where idclient=%s and clientnonvalide=%s ",(id,id))
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    def liste_portefeuille_agent(self):
        try:
            self.cur.execute("select id_portefeuille,prenom,nom from portefeuille,personnel where personnel=id_personnel ")
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)
    def enregistrer_doleance(self,id,description):
        try:
            self.cur.execute("insert into doleance(clientnonvalide,description) values (%s,%s)",(id,description))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return 0
    def liste_clientnonvalide_(self):
        try:
            self.cur.execute("select idclient,nom,prenom,telephone,adresse,activite,photo from clientnonvalide where idclient not in (select clientnonvalide from doleance)  ")
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)
    def modifier_clientnonvalide(self,id,nom,prenom,telephone,adresse,activite,sexe,date_nai,situa_matri,piece):
       try:
            self.cur.execute("update clientnonvalide set nom=%s,prenom=%s,telephone=%s,adresse=%s,activite=%s,sexe=%s,date_naissance=%s,situation_matri=%s,piece_identite=%s  where idclient=%s ",(nom,prenom,telephone,adresse,activite,sexe,date_nai,situa_matri,piece,id))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
       except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return 0
    def liste_clientnonvalide(self):
        try:
            self.cur.execute("select idclient,nom,prenom,telephone,adresse,activite,sexe,date_naissance,situation_matri,piece_identite from clientnonvalide ")
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)

    def dashboard_c_c(self):
        try:
            self.cur.execute("select c.idclient,c.nom,c.prenom,c.telephone,c.adresse,c.situation_matri,c.date_naissance,c.piece_identite,cc.solde,co.solde,ce.solde,c.portefeuille,pe.id_personnel,pe.prenom,pe.nom,c.date_creation from client c,compte_credit cc,compte_courant co,compte_epargne ce,personnel pe,portefeuille po where (c.idclient=cc.client and c.idclient=co.client and c.idclient=ce.client) and ((c.portefeuille=po.id_portefeuille) and po.personnel=pe.id_personnel) ")
            output=self.cur.fetchall()
            return output
        except Exception as e:
            print(e)
    def nbrclient(self):
        try:
            self.cur.execute("select count(idclient) from client ")
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    def nbrclientjour(self):
        try:
            self.cur.execute("select count(idclient) from clientnonvalide where date_creation=current_date")
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    def seconnecter(self,pseudo,mot_de_passe):
        try:
            self.cur.execute("select id_personnel,pseudo,mot_de_passe,fonction,nom,prenom,photo from personnel where pseudo='"+pseudo+"' and mot_de_passe='"+mot_de_passe+"'")
            output=self.cur.fetchone()
            return output
        except Exception as e:
            print(e)
    #PERSONNEL
    def enregistrer_personnel(self,nom,prenom,telephone,fonction,pseudo,mot_de_passe,photo):
        try:
            self.cur.execute("insert into personnel(nom,prenom,telephone,fonction,pseudo,mot_de_passe,photo) values (%s,%s,%s,%s,%s,%s,%s)",(nom,prenom,telephone,fonction,pseudo,mot_de_passe,photo))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return 0
    def enregistrer_clientnonvalide(self,nom,prenom,telephone,adresse,activite,date_nai,photo,sexe,situa_matri,piece):
        try:
            self.cur.execute("insert into clientnonvalide(nom,prenom,telephone,adresse,activite,date_naissance,photo,sexe,situation_matri,piece_identite) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(nom,prenom,telephone,adresse,activite,date_nai,photo,sexe,situa_matri,piece))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return e

    def liste_personnel(self):
        try:
            self.cur.execute("select nom,prenom,telephone from personnel ")
            output=self.cur.fetchall()
            return output

        except Exception as e:
            print(e)

    def modifier_personnel(self,nom,prenom,telephone,fonction,pseudo,mot_de_passe,photo,id):
       try:
            self.cur.execute("update personnel set nom=%s,prenom=%s,telephone=%s,fonction=%s,pseudo=%s,mot_de_passe=%s,photo=%s where id_personnel=%s ",(nom,prenom,telephone,fonction,pseudo,mot_de_passe,photo,id))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
       except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return 0
    def supprimer_personne(self,id):
       try:
            self.cur.execute("delete from personnel where id_personnel=%s ",(id))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
       except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return 0
    def rechercher_personne_telephone(self,telephone):
        
        self.cur.execute("select nom,prenom,telephone from personnel where telephone LIKE '%"+telephone+"%'")
        output=self.cur.fetchall()
        return output

    def enregistreportefeuille(self,montant_financer:int,personnel):
        try:
            self.cur.execute("insert into portefeuille(montant_financer,personnel) values (%s,%s)",(montant_financer,personnel))
            self.con.commit()
            print("success")
            self.con.close()
            return 1
        except Exception as e:
            print(e)
            self.con.rollback()
            self.con.close()
            return 0

class Main(MDApp):
       overlay_color = get_color_from_hex("#F6CE67FF")
       dialog = None
       dialog1=None
       dialog2=None
       dialog3=None
       id_cr=None
       def __init__(self, **kwargs):
            super().__init__(**kwargs)
            Window.bind(on_keyboard=self.events)
            self.manager_open = False
            self.file_manager = MDFileManager(
                exit_manager=self.exit_manager, select_path=self.select_path
            )
            self.screen=Builder.load_string(kv)

            #Connexion et inscription
            fonction=["Chargé(e) Clientèle","Chargé(e) d'affaire",'Caissier']
            menu_items_fonction = [
                {
                    "text": f"{i}", 
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=f"{i}": self.menu_callback_fonction(x),
                } for i in fonction
            ]
            self.menu_fonction = MDDropdownMenu(
                #caller=Inscription().ids['fonction_inscri'],
                caller=self.screen.ids["manager"].get_screen("inscription").ids["fonction_inscri"],
                items=menu_items_fonction,
                width_mult=4,
            )
            #C_C
            sexe=['Masculin','Féminin']
            menu_items_sexe = [
                {
                    "text": f"{i}", 
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=f"{i}": self.menu_callback_sexe(x),
                } for i in sexe
            ]
            self.menu_sexe = MDDropdownMenu(
                #caller=Inscription().ids['fonction_inscri'],
                caller=self.screen.ids["manager"].get_screen("c_c").ids["sexe_client"],
                items=menu_items_sexe,
                width_mult=4,
            )

            situa=['Mariée','Célibataire']
            menu_items_situa = [
                {
                    "text": f"{i}", 
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=f"{i}": self.menu_callback_situa(x),
                } for i in situa
            ]
            self.menu_situa = MDDropdownMenu(
                #caller=Inscription().ids['fonction_inscri'],
                caller=self.screen.ids["manager"].get_screen("c_c").ids["situa_matri_client"],
                items=menu_items_situa,
                width_mult=4,
            )

            piece=["Carte d'identité",'Carte Nina','Passport']
            menu_items_piece = [
                {
                    "text": f"{i}", 
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=f"{i}": self.menu_callback_piece(x),
                } for i in piece
            ]
            self.menu_piece = MDDropdownMenu(
                #caller=Inscription().ids['fonction_inscri'],
                caller=self.screen.ids["manager"].get_screen("c_c").ids["piece_client"],
                items=menu_items_piece,
                width_mult=4,
            )

            type_comptedepot=["Compte Courant","Compte d'épargne"]
            menu_items_comptedepot = [
                {
                    "text": f"{i}", 
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=f"{i}": self.menu_callback_comptedepot(x),
                } for i in type_comptedepot
            ]
            self.menu_comptedepot = MDDropdownMenu(
                #caller=Inscription().ids['fonction_inscri'],
                caller=self.screen.ids["manager"].get_screen("caissier").ids["typecompte"],
                items=menu_items_comptedepot,
                width_mult=4,
            )

            type_compteretrait=["Compte Crédit","Compte d'épargne"]
            menu_items_compteretrait = [
                {
                    "text": f"{i}", 
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=f"{i}": self.menu_callback_compteretrait(x),
                } for i in type_compteretrait
            ]
            self.menu_compteretrait = MDDropdownMenu(
                #caller=Inscription().ids['fonction_inscri'],
                caller=self.screen.ids["manager"].get_screen("caissier").ids["typecompteretrait"],
                items=menu_items_compteretrait,
                width_mult=4,
            )
       #Les Fonction file
       def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True

       def select_path(self, path: str):
        '''
        It will be called when you click on the file name
        or the catalog selection button.

        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        self.screen.ids["manager"].get_screen("inscription").ids["photo_agent"].text=path
        self.screen.ids["manager"].get_screen("c_c").ids["photo_client"].text=path
        print(path)
        toast(path)

       def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

       def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

       #CRUD CRUD CRUD CRUD CRUD CRUD CRUD CRUD CRUD CRUD CRUD CRUD CRUD CRUD CRUD CRUD CRUD CRUD CRUD CRUD
       def agent_ca(self):
           a=str(self.screen.ids["manager"].get_screen("c_a").ids["content_drawer_c_a"].ids["info_c_a"].title)
           l=a.split(' ',-1)
           print(l)
           self.id_c_a=l[2]
           print(self.id_c_a)
        
    
       def agent_caissier(self):
           
           b=str(self.screen.ids["manager"].get_screen("caissier").ids["content_drawer_caissier"].ids["info_caissier"].title)
           lb=b.split(' ',-1)
           print(lb)
           self.id_caissier=lb[2]
           print(self.id_caissier)

       
       def seconnecter(self):
           pseudo=self.screen.ids["manager"].get_screen("login").ids["pseudocon"].text
           mot_de_passe=self.screen.ids["manager"].get_screen("login").ids["mdpcon"].text
           if pseudo=="" or mot_de_passe=="":
               toast("Veuiller remplir les champs")
           else:
               a=base_de_donnees().seconnecter(pseudo=pseudo,mot_de_passe=mot_de_passe)
               if a==None:
                   toast("Pseudo ou Mot de passe incorrect")
               else:
                   toast("Vous êtes connecté")
                   if a[3]=="Chargé(e) Clientèle":
                       self.screen.ids["manager"].current="c_c"
                       print(self.screen.ids["manager"].get_screen("c_c").ids["content_drawer_c_c"].ids["info_c_c"])
                       self.screen.ids["manager"].get_screen("c_c").ids["content_drawer_c_c"].ids["info_c_c"].title="Agent N°: "+str(a[0])
                       self.screen.ids["manager"].get_screen("c_c").ids["content_drawer_c_c"].ids["info_c_c"].text=a[5]+" "+a[4]
                       self.screen.ids["manager"].get_screen("c_c").ids["content_drawer_c_c"].ids["infophoto_c_c"].source=a[6]
                       self.update_dashboard()
                       self.affiche_listeclient_dashboard()
                   elif a[3]=="Chargé(e) d'affaire":
                       self.screen.ids["manager"].current="c_a"
                       self.screen.ids["manager"].get_screen("c_a").ids["content_drawer_c_a"].ids["info_c_a"].title="Agent N°: "+str(a[0])
                       self.screen.ids["manager"].get_screen("c_a").ids["content_drawer_c_a"].ids["info_c_a"].text=a[5]+" "+a[4]
                       self.screen.ids["manager"].get_screen("c_a").ids["content_drawer_c_a"].ids["infophoto_c_a"].source=a[6]
                       self.agent_ca()
                       self.update_dashboard_ca()
                       self.info_c_a()
                       self.affiche_liste_client_c_a()
                       self.affiche_tableau_C_A()
                       self.affiche_liste_credit()
                   elif a[3]=="Caissier" :
                       self.screen.ids["manager"].current="caissier"
                       self.screen.ids["manager"].get_screen("caissier").ids["content_drawer_caissier"].ids["info_caissier"].title="Agent N°: "+str(a[0])
                       self.screen.ids["manager"].get_screen("caissier").ids["content_drawer_caissier"].ids["info_caissier"].text=a[5]+" "+a[4]
                       self.screen.ids["manager"].get_screen("caissier").ids["content_drawer_caissier"].ids["infophoto_caissier"].source=a[6]
                       self.agent_caissier()
                       self.update_dashboard_caissier()
                       self.affiche_liste_depot()
                       self.affiche_liste_transaction()
                       self.affiche_liste_retrait()
                   else :
                       self.screen.ids["manager"].current="chef"
                       self.screen.ids["manager"].get_screen("chef").ids["content_drawer_chef"].ids["info_chef"].title="Agent N°:"+str(a[0])
                       self.screen.ids["manager"].get_screen("chef").ids["content_drawer_chef"].ids["info_chef"].text=a[5]+" "+a[4]
                       self.screen.ids["manager"].get_screen("chef").ids["content_drawer_chef"].ids["infophoto_chef"].source=a[6]
       
       def update_dashboard_ca(self):
        
           statcacl=base_de_donnees().nbrclient_c_a(self.id_c_a)[0]
           self.screen.ids["manager"].get_screen("c_a").ids["statclient"].text=str(statcacl)
           statcacr=base_de_donnees().nbrcredit_c_a(self.id_c_a)[0]
           self.screen.ids["manager"].get_screen("c_a").ids["statcacr"].text=str(statcacr)
           statmontcr=base_de_donnees().sommecredit_c_a(self.id_c_a)[0]
           self.screen.ids["manager"].get_screen("c_a").ids["montcacr"].text=str(statmontcr)
           statnewclca=base_de_donnees().nbrclientnew_c_a(self.id_c_a)[0]
           self.screen.ids["manager"].get_screen("c_a").ids["statnewcacl"].text=str(statnewclca)
           statsommepaye=base_de_donnees().sommecreditpaye_c_a(self.id_c_a)[0]
           self.screen.ids["manager"].get_screen("c_a").ids["statmontpaye"].text=str(statsommepaye)
       
       def update_dashboard_caissier(self):
           statdepot=base_de_donnees().nbrdepot(self.id_caissier)[0]
           self.screen.ids["manager"].get_screen("caissier").ids["statdepot"].text=str(statdepot)
           statretrait=base_de_donnees().nbrretrait(self.id_caissier)[0]
           self.screen.ids["manager"].get_screen("caissier").ids["statretrait"].text=str(statretrait)

       def update_dashboard(self):
           staclient=base_de_donnees().nbrclient()[0]
           self.screen.ids["manager"].get_screen("c_c").ids["statclient"].text=str(staclient)
           statnew=base_de_donnees().nbrclientjour()[0]
           self.screen.ids["manager"].get_screen("c_c").ids["statnew"].text=str(statnew)
             

       def vider_champs_personne(self):
           self.screen.ids["manager"].get_screen("inscription").ids["nom_inscri"].text=""
           self.screen.ids["manager"].get_screen("inscription").ids["pseudo_inscri"].text=""
           self.screen.ids["manager"].get_screen("inscription").ids["prenom_inscri"].text=""
           self.screen.ids["manager"].get_screen("inscription").ids["mdp_inscri"].text=""
           self.screen.ids["manager"].get_screen("inscription").ids["telephone_inscri"].text=""
           self.screen.ids["manager"].get_screen("inscription").ids["confirmation_inscri"].text=""
           self.screen.ids["manager"].get_screen("inscription").ids["fonction_inscri"].text="Sélectionnez"
           self.screen.ids["manager"].get_screen("inscription").ids["photo_agent"].text=""
       def enregistrer_personnel(self):
           nom=self.screen.ids["manager"].get_screen("inscription").ids["nom_inscri"].text
           prenom=self.screen.ids["manager"].get_screen("inscription").ids["prenom_inscri"].text
           telephone=self.screen.ids["manager"].get_screen("inscription").ids["telephone_inscri"].text
           fonction=self.screen.ids["manager"].get_screen("inscription").ids["fonction_inscri"].text
           pseudo=self.screen.ids["manager"].get_screen("inscription").ids["pseudo_inscri"].text
           mot_de_passe=self.screen.ids["manager"].get_screen("inscription").ids["mdp_inscri"].text
           confirmation=self.screen.ids["manager"].get_screen("inscription").ids["confirmation_inscri"].text
           photo=self.screen.ids["manager"].get_screen("inscription").ids["photo_agent"].text
           if nom=="" or prenom=="" or telephone=="" or fonction=="Sélectionnez" or fonction=="" or pseudo=="" or mot_de_passe=="" or confirmation=="" or photo=="":
               print("Veuiller remplir les champs")
               toast("Veuiller remplir les champs")
           else:
               if mot_de_passe==confirmation:
                #toast("Tout les champs sont remplies"
                dst="image/"+prenom+""+nom+""+telephone+".png"
                #shutil.copy(photo,dst)
                #toast(dst)
                a=base_de_donnees().enregistrer_personnel(nom=nom,prenom=prenom,telephone=telephone,fonction=fonction,pseudo=pseudo,mot_de_passe=mot_de_passe,photo=dst)
                if a==1:
                        toast("success")
                        if fonction=="Chargé(e) d'affaire":
                            c=base_de_donnees().seconnecter(pseudo,mot_de_passe)
                            id=c[0]
                            base_de_donnees().enregistreportefeuille(0,id)
                            toast("un portefeuille vous a été offert")
                        shutil.copy(photo,dst)
                        self.vider_champs_personne() 
                else:
                        toast("erreur")
                        self.vider_champs_personne()
               else:
                   toast("Mot de passe incohérent")

       def vider_champs_clientnonvalide(self):
           self.screen.ids["manager"].get_screen("c_c").ids["nom_client"].text=""
           self.screen.ids["manager"].get_screen("c_c").ids["dateclient"].text=""
           self.screen.ids["manager"].get_screen("c_c").ids["prenom_client"].text=""
           self.screen.ids["manager"].get_screen("c_c").ids["photo_client"].text=""
           self.screen.ids["manager"].get_screen("c_c").ids["telephone_client"].text=""
           self.screen.ids["manager"].get_screen("c_c").ids["sexe_client"].text="Sélectionnez"
           self.screen.ids["manager"].get_screen("c_c").ids["adresse_client"].text=""
           self.screen.ids["manager"].get_screen("c_c").ids["situa_matri_client"].text="Sélectionnez"
           self.screen.ids["manager"].get_screen("c_c").ids["activite_client"].text=""
           self.screen.ids["manager"].get_screen("c_c").ids["piece_client"].text="Sélectionnez"
       def enregistrer_clientnonvalide(self):
           nom=self.screen.ids["manager"].get_screen("c_c").ids["nom_client"].text
           prenom=self.screen.ids["manager"].get_screen("c_c").ids["prenom_client"].text
           telephone=self.screen.ids["manager"].get_screen("c_c").ids["telephone_client"].text
           adresse=self.screen.ids["manager"].get_screen("c_c").ids["adresse_client"].text
           date_nai=self.screen.ids["manager"].get_screen("c_c").ids["dateclient"].text
           sexe=self.screen.ids["manager"].get_screen("c_c").ids["sexe_client"].text
           situation_matri=self.screen.ids["manager"].get_screen("c_c").ids["situa_matri_client"].text
           photo=self.screen.ids["manager"].get_screen("c_c").ids["photo_client"].text
           activite=self.screen.ids["manager"].get_screen("c_c").ids["activite_client"].text
           piece=self.screen.ids["manager"].get_screen("c_c").ids["piece_client"].text
           if nom=="" or prenom=="" or telephone=="" or adresse=="" or date_nai=="" or sexe=="Sélectionnez" or situation_matri=="Sélectionnez" or piece=="Sélectionnez" or activite=="" or photo=="":
               toast("Veuiller remplir les champs")
           else:
               
                #toast("Tout les champs sont remplies"
                dst="image/Client"+prenom+""+nom+""+telephone+".png"
                #shutil.copy(photo,dst)
                #toast(dst)
                a=base_de_donnees().enregistrer_clientnonvalide(nom=nom,prenom=prenom,telephone=telephone,adresse=adresse,date_nai=date_nai,situa_matri=situation_matri,activite=activite,sexe=sexe,piece=piece,photo=dst)
                if a==1:
                        toast("success")    
                        shutil.copy(photo,dst)
                        self.vider_champs_clientnonvalide() 
                        self.affiche_listeclientnonvalide()
                        self.remove_panel()
                        self.listeclientdoleance_c_c()
                else:
                        toast("erreur")
                        self.vider_champs_clientnonvalide()
              




       def listeclientdoleance_c_c(self):
           liste=base_de_donnees().liste_clientnonvalide_()
           self.mespanel=[]
           for i in liste:
             print(str(i[6]))
             id=i[0]
             self.panel=MDExpansionPanel(
                    icon=os.path.join(str(i[6])),
                    content=Content_c_c(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text=str(i[0])+" "+i[2]+" "+i[1],
                        secondary_text="   "+i[4]+", "+i[3],
                        tertiary_text="   "+"Activité: "+i[5],
                    ),
                    #on_open=self.on_panel_open
                    #check_open_panel=self.on_panel_open
                )
             self.mespanel.append(self.panel)
             self.screen.ids["manager"].get_screen("c_c").ids["box"].add_widget(self.panel)
       def remove_panel(self):
           for i in self.mespanel:
            self.screen.ids["manager"].get_screen("c_c").ids['box'].remove_widget(i)
       def on_panel_open(self,instance_panel,inst_content):
           text=str(instance_panel.panel_cls.text).split(' ',-1)
           id=int(text[0])
           description=inst_content.ids["champ"].text
           a=base_de_donnees().enregistrer_doleance(id=id,description=description)
           print(id)
           print(inst_content.ids["champ"].text)
           if a==1:
                self.screen.ids["manager"].get_screen("c_c").ids['box'].remove_widget(instance_panel)
                toast('Doleance enregistré')
                self.affiche_listeclientnonvalide_chef()
                #self.listeclientdoleance_c_c()
           #return instance_panel
    
       def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Doléance:",
                type="custom",
                content_cls=Content_Dialog_c_c(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.ferme_dialog
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()
       def ferme_dialog(self,inst):
        self.dialog.dismiss()
       '''def liste(self):
           for i in range(10):
               ListItemWithCheckbox(text="text !!!")
               a=list().insert(ListItemWithCheckbox())
           return a'''
       def show_confirmation_dialog1(self):
        if not self.dialog1:
            listecheck=[]
            liste=base_de_donnees().client_c_a(self.id_c_a)
            for i in liste:
                itemcheck=ListItemWithCheckbox(text=str(i[0])+"  "+i[1]+"  "+i[2]+"  "+i[3])
                listecheck.append(itemcheck)
            self.dialog1 = MDDialog(
                title="Clients:",
                type="confirmation",
                items=listecheck,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.ferme_dialog1
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.get_client1
                    ),
                ],
            )
        self.dialog1.open()
       def get_client1(self,inst):
           for item in self.dialog1.items:
               if item.ids.check.active == True :
                self.screen.ids["manager"].get_screen("c_a").ids['valeurcrdtcl'].text=item.text
           self.dialog1.dismiss()
           self.dialog1=None
       def ferme_dialog1(self,inst):
        self.dialog1.dismiss()
       
       def show_confirmation_dialog2(self):
        if not self.dialog2:
            listecheck=[]
            liste=base_de_donnees().liste_portefeuille_agent()
            for i in liste:
                itemcheck=ListItemWithCheckbox(text=str(i[0])+" "+i[1]+" "+i[2])
                listecheck.append(itemcheck)
            self.dialog2 = MDDialog(
                title="Portefeuille:",
                type="confirmation",
                items=listecheck,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.ferme_dialog2
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.get_client2
                    ),
                ],
            )
        self.dialog2.open()
       def get_client2(self,inst):
           for item in self.dialog2.items:
               if item.ids.check.active == True :
                self.screen.ids["manager"].get_screen("chef").ids['choix_por'].text=item.text
           self.dialog2.dismiss()
           self.dialog2=None
       def ferme_dialog2(self,inst):
        self.dialog2.dismiss()
      
       def show_confirmation_dialog3(self):
        if not self.dialog3:
            self.content=Content_Dialog_caissier()
            liste=base_de_donnees().client_caissier()
            for i in liste:
                self.content.ids['boxcldepot'].add_widget(ListItemWithCheckbox_caissier(text=str(i[0])+"  "+i[2]+" "+i[1],secondary_text="    "+i[3]))
                
                
            self.dialog3 = MDDialog(
                title="Clients:",
                type="custom",
                #items=[ListItemWithCheckbox(text="1"),ListItemWithCheckbox(text="2")],
                content_cls=self.content,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.ferme_dialog3
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.ferme_dialog3
                    ),
                ],
            )
            l=self.content.ids
            print(l)
        self.dialog3.open()
       def recherche_dialog3(self,text,widget):
           
           for j in widget.children:
             print(j)
             self.content.ids['boxcldepot'].remove_widget(j)
           liste=base_de_donnees().client_caissier_recherche(text)
           for i in liste:
               self.content.ids['boxcldepot'].add_widget(ListItemWithCheckbox_caissier(text=str(i[0])+"  "+i[2]+" "+i[1],secondary_text="    "+i[3]))
                
           
           
       def get_client3(self,text,scdtext):
           print(text)
           print(scdtext)
           self.screen.ids["manager"].get_screen("caissier").ids['cldepot'].text=text+" "+scdtext
           self.screen.ids["manager"].get_screen("caissier").ids['clretrait'].text=text+" "+scdtext
           #self.screen.ids["manager"].get_screen("caissier").ids['cldepot'].text=item.text
           #self.dialog3.dismiss()
           #self.dialog3=None
       def ferme_dialog3(self,inst):
        self.dialog3.dismiss()
       '''def text(self):
            
            #print(Inscription().children)
            #mana().get_screen()
            print(self.screen.ids["manager"].get_screen("inscription").ids["nom_inscri"].text)'''
       def menu_callback_fonction(self, text_item):
            self.screen.ids["manager"].get_screen("inscription").ids["fonction_inscri"].text=text_item
            print(text_item)
       def menu_callback_sexe(self, text_item):
            self.screen.ids["manager"].get_screen("c_c").ids["sexe_client"].text=text_item
            print(text_item)
       def menu_callback_situa(self, text_item):
            self.screen.ids["manager"].get_screen("c_c").ids["situa_matri_client"].text=text_item
            print(text_item)
       def menu_callback_piece(self, text_item):
            self.screen.ids["manager"].get_screen("c_c").ids["piece_client"].text=text_item
            print(text_item)
       def menu_callback_comptedepot(self, text_item):
            self.screen.ids["manager"].get_screen("caissier").ids["typecompte"].text=text_item
            print(text_item)
            
       def menu_callback_compteretrait(self, text_item):
            self.screen.ids["manager"].get_screen("caissier").ids["typecompteretrait"].text=text_item
            print(text_item)
       def retour(self):
           manager=self.screen.ids["manager"].get_screen("caissier").ids
           print(manager)
           #manager.current="depot_caissier"
       def create_datatable_tableau_C_C(self):
           self.data_tablenaiss=MDDataTable(
               size_hint=(0.01,0.45),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(30),lambda *args:print("Numéro de l'acte")),
                   ("Nom",dp(30)),
                   ("Prénom",dp(30)),
                   ("Téléphone",dp(40)),
                   ("Adresse",dp(30)),
                   ("Situation Matrimoniale",dp(40)),
                   ("Date Naissance",dp(30)),
                   ("Pièce",dp(40)),
                   ("Compte_Crédit",dp(40)),
                   ("Compte_Courant",dp(40)),
                   ("Compte_Epargne",dp(40)),
                   ("Portefeuille",dp(30)),
                   ("Agent",dp(50)),
                   ("Actif depuis",dp(30)),
                 
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids["manager"].get_screen("c_c").ids['tableau_bord_C_C'].add_widget(self.data_tablenaiss)
       def remove_listeclient_dashboard(self):
           self.screen.ids["manager"].get_screen("c_c").ids['tableau_bord_C_C'].remove_widget(self.data_tablenaiss)
       def affiche_listeclient_dashboard_search(self):
           text=self.screen.ids["manager"].get_screen("c_c").ids["research_dash"].text
           self.remove_listeclient_dashboard()
           self.create_datatable_tableau_C_C()
           #self.data_tablenaiss.row_data=base_de_donnees().dashboard_c_c()
           liste=base_de_donnees().dashboard_c_c_search(text)
           l_cl=[]
           for i in liste:
               Num=i[0]
               nom=i[1]
               prenom=i[2]
               telephone=i[3]
               adresse=i[4]
               sitma=i[5]
               datenai=i[6]
               piece=i[7]
               credit=i[8]
               courant=i[9]
               epargne=i[10]
               portefeuille=i[11]
               agent=str(i[12])+" "+i[13]+" "+i[14]
               actif=i[15]
               l=[Num,nom,prenom,telephone,adresse,sitma,datenai,piece,credit,courant,epargne,portefeuille,agent,actif]
               l_cl.append(l)
           self.data_tablenaiss.row_data=l_cl
       def affiche_listeclient_dashboard(self):
           self.remove_listeclient_dashboard()
           self.create_datatable_tableau_C_C()
           #self.data_tablenaiss.row_data=base_de_donnees().dashboard_c_c()
           liste=base_de_donnees().dashboard_c_c()
           l_cl=[]
           for i in liste:
               Num=i[0]
               nom=i[1]
               prenom=i[2]
               telephone=i[3]
               adresse=i[4]
               sitma=i[5]
               datenai=i[6]
               piece=i[7]
               credit=i[8]
               courant=i[9]
               epargne=i[10]
               portefeuille=i[11]
               agent=str(i[12])+" "+i[13]+" "+i[14]
               actif=i[15]
               l=[Num,nom,prenom,telephone,adresse,sitma,datenai,piece,credit,courant,epargne,portefeuille,agent,actif]
               l_cl.append(l)
           self.data_tablenaiss.row_data=l_cl
       def create_datatable_tableau_C_A(self):
           self.data_tablenaiss_c_a=MDDataTable(
               size_hint=(0.01,0.35),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(30),lambda *args:print("Numéro de l'acte")),
                   ("Nom",dp(30)),
                   ("Prénom",dp(30)),
                   ("Téléphone",dp(40)),
                   ("Montant_Credit",dp(30)),
                   ("Montant_payé",dp(40)),
                   ("Montant_restant",dp(40)),
                   ("Date_Echéance",dp(40)),
                 
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids["manager"].get_screen("c_a").ids['tableau_bord_C_A'].add_widget(self.data_tablenaiss_c_a)
       def remove_tableau_C_A(self):
           self.screen.ids["manager"].get_screen("c_a").ids['tableau_bord_C_A'].remove_widget(self.data_tablenaiss_c_a)
       def affiche_tableau_C_A(self):
           id=int(self.id_c_a)
           self.remove_tableau_C_A()
           self.create_datatable_tableau_C_A()
           l=base_de_donnees().clients_dash_c_a(id)
           print(l)
           self.data_tablenaiss_c_a.row_data=base_de_donnees().clients_dash_c_a(id)

       def create_datatable_liste_clientnonvalide(self):
           self.data_tablenaiss_cl=MDDataTable(
               size_hint=(0.01,0.40),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(20),lambda *args:print("Numéro de l'acte")),
                   ("Nom",dp(30)),
                   ("Prénom",dp(30)),
                   ("Téléphone",dp(40)),
                   ("Adresse",dp(30)),
                   ("Activité",dp(40)),
                   ("sexe",dp(20)),
                   ("Date_Naiss",dp(40)),
                   ("Situa_Matri",dp(30)),
                   ("Pièce",dp(40)),
                   
                 
               ],
               background_color_header="grey",
               row_data=[],
            )
           self.data_tablenaiss_cl.bind(on_check_press=self.on_check_press_listeclientnonvalide)
           self.screen.ids["manager"].get_screen("c_c").ids['liste_client_tab'].add_widget(self.data_tablenaiss_cl)
       def on_check_press_listeclientnonvalide(self,instance_table,current_row):
           self.idclientnonvalide=int(current_row[0])
           self.screen.ids["manager"].get_screen("c_c").ids["nom_client"].text=current_row[1]
           self.screen.ids["manager"].get_screen("c_c").ids["dateclient"].text=current_row[7]
           self.screen.ids["manager"].get_screen("c_c").ids["prenom_client"].text=current_row[2]
           #self.screen.ids["manager"].get_screen("c_c").ids["photo_client"].text=current_row[1]
           self.screen.ids["manager"].get_screen("c_c").ids["telephone_client"].text=current_row[3]
           self.screen.ids["manager"].get_screen("c_c").ids["sexe_client"].text=current_row[6]
           self.screen.ids["manager"].get_screen("c_c").ids["adresse_client"].text=current_row[4]
           self.screen.ids["manager"].get_screen("c_c").ids["situa_matri_client"].text=current_row[8]
           self.screen.ids["manager"].get_screen("c_c").ids["activite_client"].text=current_row[5]
           self.screen.ids["manager"].get_screen("c_c").ids["piece_client"].text=current_row[9]
       def remove_listeclientnonvalide(self):
           self.screen.ids["manager"].get_screen("c_c").ids['liste_client_tab'].remove_widget(self.data_tablenaiss_cl)
       def affiche_listeclientnonvalide(self):
           self.remove_listeclientnonvalide()
           self.create_datatable_liste_clientnonvalide()
           self.data_tablenaiss_cl.row_data=base_de_donnees().liste_clientnonvalide()
       def affiche_listeclientnonvalide_search(self):
           text=self.screen.ids["manager"].get_screen("c_c").ids["research_client_cc"].text
           self.remove_listeclientnonvalide()
           self.create_datatable_liste_clientnonvalide()
           self.data_tablenaiss_cl.row_data=base_de_donnees().liste_clientnonvalide_search(text)
       def modifier_clientnonvalide(self):
           nom=self.screen.ids["manager"].get_screen("c_c").ids["nom_client"].text
           prenom=self.screen.ids["manager"].get_screen("c_c").ids["prenom_client"].text
           telephone=self.screen.ids["manager"].get_screen("c_c").ids["telephone_client"].text
           adresse=self.screen.ids["manager"].get_screen("c_c").ids["adresse_client"].text
           date_nai=self.screen.ids["manager"].get_screen("c_c").ids["dateclient"].text
           sexe=self.screen.ids["manager"].get_screen("c_c").ids["sexe_client"].text
           situation_matri=self.screen.ids["manager"].get_screen("c_c").ids["situa_matri_client"].text
           photo=self.screen.ids["manager"].get_screen("c_c").ids["photo_client"].text
           activite=self.screen.ids["manager"].get_screen("c_c").ids["activite_client"].text
           piece=self.screen.ids["manager"].get_screen("c_c").ids["piece_client"].text
           a=base_de_donnees().modifier_clientnonvalide(nom=nom,prenom=prenom,telephone=telephone,adresse=adresse,activite=activite,sexe=sexe,date_nai=date_nai,situa_matri=situation_matri,piece=piece,id=self.idclientnonvalide)
           if a==1:
               toast("modifié")
               self.affiche_listeclientnonvalide()
               self.vider_champs_clientnonvalide() 
           else:
               
               toast("ce numéro de téléphone éxiste déjà")

       def create_datatable_liste_clientnonvalide_chef(self):
           self.data_table_chef=MDDataTable(
               size_hint=(0.01,1),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(20),lambda *args:print("Numéro de l'acte")),
                   ("Nom",dp(30)),
                   ("Prénom",dp(30)),
                   ("Téléphone",dp(40)),
                   ("Adresse",dp(30)),
                   ("Activité",dp(40)),
                   ("sexe",dp(20)),
                   ("Date_Naiss",dp(40)),
                   ("Situa_Matri",dp(30)),
                   ("Pièce",dp(40)),
                   
                 
               ],
               background_color_header="grey",
               row_data=[],
            )
           self.data_table_chef.bind(on_check_press=self.on_check_press_listeclientnonvalide_chef)
           self.screen.ids["manager"].get_screen("chef").ids['datatablevalide'].add_widget(self.data_table_chef)
       def on_check_press_listeclientnonvalide_chef(self,instance_table,current_row):
           self.id_=current_row[0]
           self.nom_=current_row[1]
           self.prenom_=current_row[2]
           self.telephone_=current_row[3]
           self.adresse_=current_row[4]
           self.activite_=current_row[5]
           self.sexe_=current_row[6]
           self.date_=current_row[7]
           self.situa_=current_row[8]
           self.piece_=current_row[9]
           l=base_de_donnees().liste_clientnonvalide_dol(self.id_)
           self.photo_=l[0]
           self.screen.ids["manager"].get_screen("chef").ids['photo_cl'].source=l[0]
           self.screen.ids["manager"].get_screen("chef").ids['descr'].text=l[1]
       def remove_listeclientnonvalide_chef(self):
           self.screen.ids["manager"].get_screen("chef").ids['datatablevalide'].remove_widget(self.data_table_chef)
       def enregistre_listeclientnonvalide_chef(self):
           p=str(self.screen.ids["manager"].get_screen("chef").ids['choix_por'].text)
           l=p.split(' ',-1)
           portefeuille_=int(l[0])
           a=base_de_donnees().enregistrer_client(self.nom_,self.prenom_,self.telephone_,self.adresse_,self.activite_,self.date_,self.photo_,self.sexe_,self.situa_,self.piece_,portefeuille_)
           if a==1:
               id=base_de_donnees().idclient(self.telephone_)[0]
               base_de_donnees().enregistrecomptecourant(id)
               base_de_donnees().enregistrecomptecredit(id)
               base_de_donnees().enregistrecompteepargne(id)
               self.screen.ids["manager"].get_screen("chef").ids['photo_cl'].source="image/photo.png"
               self.screen.ids["manager"].get_screen("chef").ids['descr'].text=""
               self.screen.ids["manager"].get_screen("chef").ids['choix_por'].text=""
               self.affiche_listeclient_dashboard()
               self.affiche_listeclientnonvalide_chef()
               #self.update_dashboard()
               toast('Success')
       def affiche_listeclientnonvalide_chef(self):
           self.remove_listeclientnonvalide_chef()
           self.create_datatable_liste_clientnonvalide_chef()
           self.data_table_chef.row_data=base_de_donnees().liste_clientnonvalide_doleance()


       def create_datatable_liste_credit(self):
           self.data_tablenaiss_c=MDDataTable(
               size_hint=(0.01,0.40),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(20),lambda *args:print("Numéro de l'acte")),
                   ("Montant_crédit",dp(30)),
                   ("Montant_payé",dp(30)),
                   ("montant_restant",dp(40)),
                   ("Date_approbation",dp(40)),
                   ("Date_echeance",dp(40)),
                   ("Période",dp(20)),
                   ("Paiement_tranche",dp(40)),
                   ("client",dp(70)),
                   ("Etat",dp(40)),
                   
                 
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.data_tablenaiss_c.bind(on_check_press=self.on_check_press_liste_credit)
           self.screen.ids["manager"].get_screen("c_a").ids['liste_credit_tab'].add_widget(self.data_tablenaiss_c)
       def on_check_press_liste_credit(self,instance_table,current_row):
           self.id_cr=current_row[0]
           self.screen.ids["manager"].get_screen("c_a").ids["montant_credit_c_a"].text=current_row[1]
           self.screen.ids["manager"].get_screen("c_a").ids["datecrd"].text=current_row[5]
           self.screen.ids["manager"].get_screen("c_a").ids["periode"].text=current_row[6]
           self.screen.ids["manager"].get_screen("c_a").ids["montant"].text=current_row[7]
           self.screen.ids["manager"].get_screen("c_a").ids['valeurcrdtcl'].text=current_row[8]
       def modifier_liste_credit(self):
           p=str(self.screen.ids["manager"].get_screen("c_a").ids['valeurcrdtcl'].text)
           
           montant_credit=self.screen.ids["manager"].get_screen("c_a").ids["montant_credit_c_a"].text
           periode_rem=self.screen.ids["manager"].get_screen("c_a").ids["periode"].text
           montant_rem=self.screen.ids["manager"].get_screen("c_a").ids["montant"].text
           date_echean=self.screen.ids["manager"].get_screen("c_a").ids["datecrd"].text
           
           if montant_credit=="" or periode_rem=="" or montant_rem=="" or date_echean=="" or p=="aucun client n'est selectionné" or self.id_cr==None:
               toast("aucun credit n'est selectionné")
           else:
               l=p.split('  ',-1)
               taille=l.__len__()
               if taille==3:
                   client_tel=l[2]
                   print(client_tel)
                   id_cl=base_de_donnees().tel_cl(client_tel)[0]
                   print(id_cl)
                   a=base_de_donnees().update_credit(int(montant_credit),int(periode_rem),int(montant_rem),date_echean,int(self.id_cr),int(id_cl))
                   if a==1:
                       base_de_donnees().updatecompte_update_credit(int(montant_credit),int(id_cl))
                       toast("Crédit modifié")
                       self.affiche_liste_credit()
                       self.screen.ids["manager"].get_screen("c_a").ids["montant_credit_c_a"].text=""
                       self.screen.ids["manager"].get_screen("c_a").ids["periode"].text=""
                       self.screen.ids["manager"].get_screen("c_a").ids["montant"].text=""
                       self.screen.ids["manager"].get_screen("c_a").ids["datecrd"].text=""
                       self.screen.ids["manager"].get_screen("c_a").ids['valeurcrdtcl'].text="aucun client n'est selectionné"
                       self.data_tablenaiss_c_a()
                       self.info_c_a()
                       self.affiche_liste_client_c_a()
                       self.affiche_tableau_C_A()

               else:
                   id_cl_=l[0]
                   print(id_cl_)
                   a=base_de_donnees().update_credit(int(montant_credit),int(periode_rem),int(montant_rem),date_echean,int(self.id_cr),int(id_cl_))
                   if a==1:
                       base_de_donnees().updatecompte_update_credit(int(montant_credit),int(id_cl_))
                       toast("Crédit modifié")
                       self.affiche_liste_credit()
                       self.screen.ids["manager"].get_screen("c_a").ids["montant_credit_c_a"].text=""
                       self.screen.ids["manager"].get_screen("c_a").ids["periode"].text=""
                       self.screen.ids["manager"].get_screen("c_a").ids["montant"].text=""
                       self.screen.ids["manager"].get_screen("c_a").ids["datecrd"].text=""
                       self.screen.ids["manager"].get_screen("c_a").ids['valeurcrdtcl'].text="aucun client n'est selectionné"
                       self.info_c_a()
                       self.affiche_liste_client_c_a()
                       self.affiche_tableau_C_A()
               

       def remove_liste_credit(self):
           self.screen.ids["manager"].get_screen("c_a").ids['liste_credit_tab'].remove_widget(self.data_tablenaiss_c)
       def enregistre_liste_credit(self):
           p=str(self.screen.ids["manager"].get_screen("c_a").ids['valeurcrdtcl'].text)
           
           montant_credit=self.screen.ids["manager"].get_screen("c_a").ids["montant_credit_c_a"].text
           periode_rem=self.screen.ids["manager"].get_screen("c_a").ids["periode"].text
           montant_rem=self.screen.ids["manager"].get_screen("c_a").ids["montant"].text
           date_echean=self.screen.ids["manager"].get_screen("c_a").ids["datecrd"].text
           portefeuille=self.screen.ids["manager"].get_screen("c_a").ids["numportefeuille"].text
           if montant_credit=="" or periode_rem=="" or montant_rem=="" or date_echean=="" or p=="aucun client n'est selectionné":
               toast("Veullez remplir les champs")
           else:
               l=p.split('  ',-1)
               client=int(l[0])
               print(client)
               base_de_donnees().enregistrer_credit(int(montant_credit),int(periode_rem),int(montant_rem),date_echean,client,int(portefeuille),self.id_c_a)
               toast("Crédit enregistré")
               base_de_donnees().updatecompte_credit(int(montant_credit),client)
               
               self.affiche_liste_credit()
               self.screen.ids["manager"].get_screen("c_a").ids["montant_credit_c_a"].text=""
               self.screen.ids["manager"].get_screen("c_a").ids["periode"].text=""
               self.screen.ids["manager"].get_screen("c_a").ids["montant"].text=""
               self.screen.ids["manager"].get_screen("c_a").ids["datecrd"].text=""
               self.screen.ids["manager"].get_screen("c_a").ids['valeurcrdtcl'].text="aucun client n'est selectionné"
               self.info_c_a()
               self.affiche_liste_client_c_a()
               self.affiche_tableau_C_A()

       def info_c_a(self):
           a=base_de_donnees().info_c_a(self.id_c_a)
           nbcr=base_de_donnees().nbrcredit_c_a(self.id_c_a)[0]
           nbcl=base_de_donnees().nbrclient_c_a(self.id_c_a)[0]
           montant=base_de_donnees().sommecredit_c_a(self.id_c_a)[0]
           self.screen.ids["manager"].get_screen("c_a").ids["agent"].source=self.screen.ids["manager"].get_screen("c_a").ids["content_drawer_c_a"].ids["infophoto_c_a"].source
           self.screen.ids["manager"].get_screen("c_a").ids["numagent"].text=str(a[0])
           self.screen.ids["manager"].get_screen("c_a").ids["nomagent"].text=a[1]
           self.screen.ids["manager"].get_screen("c_a").ids["prenomagent"].text=a[2]
           self.screen.ids["manager"].get_screen("c_a").ids["numportefeuille"].text=str(a[3])
           self.screen.ids["manager"].get_screen("c_a").ids["nbrcdt"].text=str(nbcr)
           self.screen.ids["manager"].get_screen("c_a").ids["nbrcl"].text=str(nbcl)
           self.screen.ids["manager"].get_screen("c_a").ids["montantfin"].text=str(montant)


       def affiche_liste_credit(self):
           self.remove_liste_credit()
           self.create_datatable_liste_credit()
           liste=base_de_donnees().liste_credits(self.id_c_a)
           l_cl=[]
           for i in liste:
               Num=i[0]
               montantcredit=i[1]
               montantpaye=i[2]
               montantreste=i[3]
               date_appr=i[4]
               date_echeance=i[5]
               periode=i[6]
               montant_rem=i[7]
               client=i[8]+"  "+i[9]+"  "+i[10]
               etat=i[11]
               
               l=[Num,montantcredit,montantpaye,montantreste,date_appr,date_echeance,periode,montant_rem,client,etat]
               l_cl.append(l)
           self.data_tablenaiss_c.row_data=l_cl
           

       def create_datatable_liste_client_c_a(self):
           self.data=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(30),lambda *args:print("Numéro de l'acte")),
                   ("Nom",dp(40)),
                   ("Prénom",dp(40)),
                   ("Téléphone",dp(40)),
                   ("Adresse",dp(30)),
                   ("Activité",dp(40)),
                   ("Nombre Crédit",dp(40)),
                   ("Date",dp(40)),
                 
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids["manager"].get_screen("c_a").ids['liste'].add_widget(self.data)
       def remove_liste_client_c_a(self):
           self.screen.ids["manager"].get_screen("c_a").ids['liste'].remove_widget(self.data)
       def affiche_liste_client_c_a(self):
           id=int(self.id_c_a)
           self.remove_liste_client_c_a()
           self.create_datatable_liste_client_c_a()
           l=base_de_donnees().clients_c_a(id)
           print(l)
           self.data.row_data=base_de_donnees().clients_c_a(id)

       def create_datatable_dash(self):
           self.data_caissier=MDDataTable(
               size_hint=(0.01,0.4),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(30),lambda *args:print("Numéro de l'acte")),
                   ("Client",dp(60)),
                   ("Type_Transaction",dp(40)),
                   ("Montant",dp(40)),
                   ("Compte",dp(40)),
                   ("Date",dp(40)),
                   
                 
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids["manager"].get_screen("caissier").ids['tableau_bord_CAISSIER'].add_widget(self.data_caissier)
       def remove_liste_transaction(self):
           self.screen.ids["manager"].get_screen("caissier").ids['tableau_bord_CAISSIER'].remove_widget(self.data_caissier)
       
       def affiche_liste_transaction(self):
           id=int(self.id_caissier)
           self.remove_liste_transaction()
           self.create_datatable_dash()
           l=base_de_donnees().liste_transaction(id)
           print(l)
           l_cl=[]
           for i in l:
               Num=i[0]
               client=i[2]+"  "+i[1]+"  "+i[3]
               type_trans=i[4]
               montant=i[5]
               type_compte=i[6]
               date=i[7]
               
               
               li=[Num,client,type_trans,montant,type_compte,date]
               l_cl.append(li)
           self.data_caissier.row_data=l_cl

       def create_datatable_depot(self):
           self.data_depot=MDDataTable(
               size_hint=(0.01,.95),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(30),lambda *args:print("Numéro de l'acte")),
                   ("Client",dp(60)),
                   ("Type_Transaction",dp(40)),
                   ("Montant",dp(40)),
                   ("Compte",dp(40)),
                   ("Date",dp(40)),
                   
                 
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids["manager"].get_screen("caissier").ids['liste_depot'].add_widget(self.data_depot)
       def remove_liste_depot(self):
           self.screen.ids["manager"].get_screen("caissier").ids['liste_depot'].remove_widget(self.data_depot)
       def enregistre_depot(self):
           p=str(self.screen.ids["manager"].get_screen("caissier").ids['cldepot'].text)
           
           type_copmte=self.screen.ids["manager"].get_screen("caissier").ids["typecompte"].text
           montant=self.screen.ids["manager"].get_screen("caissier").ids["montantdepot"].text
           if type_copmte=="" or montant=="" or p=="aucun client n'est selectionné":
               toast("Veullez remplir les champs")
           else:
               l=p.split('  ',-1)
               client=int(l[0])
               print(client)
               depot='dépôt'
               if type_copmte=="Compte Courant":
                base_de_donnees().enregistrer_transaction(client,type_copmte,depot,int(montant),int(self.id_caissier))
                base_de_donnees().updatecompte_courant(int(montant),client)
                toast("Dépôt enregistré")
                self.affiche_liste_depot()
                self.affiche_liste_transaction()
                self.screen.ids["manager"].get_screen("caissier").ids['cldepot'].text="aucun client n'est selectionné"
                self.screen.ids["manager"].get_screen("caissier").ids["typecompte"].text='Sélectionnez'
                self.screen.ids["manager"].get_screen("caissier").ids["montantdepot"].text=""
                
               if type_copmte=="Compte d'épargne":
                base_de_donnees().enregistrer_transaction(client,type_copmte,depot,int(montant),int(self.id_caissier))
                base_de_donnees().updatecompte_epargne(int(montant),client)
                toast("Dépôt enregistré")
                self.affiche_liste_depot()
                self.affiche_liste_transaction()
                self.screen.ids["manager"].get_screen("caissier").ids['cldepot'].text="aucun client n'est selectionné"
                self.screen.ids["manager"].get_screen("caissier").ids["typecompte"].text='Sélectionnez'
                self.screen.ids["manager"].get_screen("caissier").ids["montantdepot"].text=""
                
       def affiche_liste_depot(self):
           self.remove_liste_depot()
           self.create_datatable_depot()
           liste=base_de_donnees().liste_depot()
           l_cl=[]
           for i in liste:
               Num=i[0]
               client=i[2]+"  "+i[1]+"  "+i[3]
               type_trans=i[4]
               montant=i[5]
               type_compte=i[6]
               date=i[7]
               
               
               l=[Num,client,type_trans,montant,type_compte,date]
               l_cl.append(l)
           self.data_depot.row_data=l_cl

       def create_datatable_retrait(self):
           self.data_retrait=MDDataTable(
               size_hint=(0.01,.95),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(30),lambda *args:print("Numéro de l'acte")),
                   ("Client",dp(60)),
                   ("Type_Transaction",dp(40)),
                   ("Montant",dp(40)),
                   ("Compte",dp(40)),
                   ("Date",dp(40)),
                   
                 
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids["manager"].get_screen("caissier").ids['liste_retrait'].add_widget(self.data_retrait)

       def remove_liste_retrait(self):
           self.screen.ids["manager"].get_screen("caissier").ids['liste_retrait'].remove_widget(self.data_retrait)
       def enregistre_retrait(self):
           p=str(self.screen.ids["manager"].get_screen("caissier").ids['clretrait'].text)
           
           type_copmte=self.screen.ids["manager"].get_screen("caissier").ids["typecompteretrait"].text
           montant=self.screen.ids["manager"].get_screen("caissier").ids["montantretrait"].text
           if type_copmte=="" or montant=="" or p=="aucun client n'est selectionné":
               toast("Veullez remplir les champs")
           else:
               l=p.split('  ',-1)
               client=int(l[0])
               print(client),
               retrait='retrait'
               if type_copmte=="Compte Crédit":
                solde=base_de_donnees().verifier_compte_credit(client)[0]
                if solde<int(montant):
                    toast("Votre solde est insuffisant pour effectuer ce retrait")
                elif solde>=int(montant):
                    base_de_donnees().enregistrer_transaction(client,type_copmte,retrait,int(montant),int(self.id_caissier))
                    base_de_donnees().updatecompte_credit_retrait(int(montant),client)
                    toast("success")
                    self.affiche_liste_retrait()
                    self.affiche_liste_transaction()
                    self.screen.ids["manager"].get_screen("caissier").ids['clretrait'].text="aucun client n'est selectionné"
                    self.screen.ids["manager"].get_screen("caissier").ids["typecompteretrait"].text='Sélectionnez'
                    self.screen.ids["manager"].get_screen("caissier").ids["montantretrait"].text=""
                
               if type_copmte=="Compte d'épargne":
                solde=base_de_donnees().verifier_compte_epargne(client)[0]
                if solde<int(montant):
                    toast("Votre solde est insuffisant pour effectuer ce retrait")
                elif solde>=int(montant):
                    base_de_donnees().enregistrer_transaction(client,type_copmte,retrait,int(montant),int(self.id_caissier))
                    base_de_donnees().updatecompte_epargne_retrait(int(montant),client)
                    toast("success")
                    self.affiche_liste_retrait()
                    self.affiche_liste_transaction()
                    self.screen.ids["manager"].get_screen("caissier").ids['clretrait'].text="aucun client n'est selectionné"
                    self.screen.ids["manager"].get_screen("caissier").ids["typecompteretrait"].text='Sélectionnez'
                    self.screen.ids["manager"].get_screen("caissier").ids["montantretrait"].text=""
                
       def affiche_liste_retrait(self):
           self.remove_liste_retrait()
           self.create_datatable_retrait()
           liste=base_de_donnees().liste_retrait()
           l_cl=[]
           for i in liste:
               Num=i[0]
               client=i[2]+"  "+i[1]+"  "+i[3]
               type_trans=i[4]
               montant=i[5]
               type_compte=i[6]
               date=i[7]
               
               
               l=[Num,client,type_trans,montant,type_compte,date]
               l_cl.append(l)
           self.data_retrait.row_data=l_cl    


       def show_date_picker_c_c(self):
          date_dialog = MDDatePicker()
          date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
          date_dialog.md_bg_color="#F6CE67FF"
          
          date_dialog.open()
       def on_save(self, instance, value, date_range):

        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        self.screen.ids["manager"].get_screen("c_c").ids["dateclient"].text=str(value)
        self.screen.ids["manager"].get_screen("c_a").ids["datecrd"].text=str(value)
        
        
        print(instance, value, date_range)

       def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
       def build(self):
          self.create_datatable_tableau_C_C()
          self.create_datatable_liste_clientnonvalide() 
          self.create_datatable_liste_clientnonvalide_chef()
          self.create_datatable_tableau_C_A()
          self.create_datatable_liste_client_c_a()
          self.create_datatable_liste_credit()
          self.create_datatable_depot()
          self.create_datatable_retrait()
          self.listeclientdoleance_c_c()
          self.create_datatable_dash()
          #self.update_dashboard()
          self.affiche_listeclient_dashboard()
          self.affiche_listeclientnonvalide()
          self.affiche_listeclientnonvalide_chef()
          base_de_donnees()
          return self.screen



       
'''Config.set('graphics','fullscreen','auto')
Config.set('graphics','window_state','maximized')
Config.write()'''            


Main().run()
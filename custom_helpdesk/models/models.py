# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class HelpdeskTeamInherit(models.Model):
    _inherit = 'helpdesk.team'

    equipe = fields.Selection([('service_clientele', 'Service Clientèle'),
                              ('support_rh', 'Support RH'),
                              ], string='Equipe')


class HelpdeskStageInherit(models.Model):
    _inherit = 'helpdesk.stage'


    etape =fields.Selection([('traitement_prestataire', 'Traitement prestataire'), ('preparation_coordinateur_it', 'Préparation Coordinateur IT'),
                             ('demande_rh', 'Demande RH'), ('preparation_prestataire', 'Préparation Prestataire'),('traitement_manager', 'Traitement Manager'),
                             ('Preparation_materiel_interne', 'Préparation matériel interne'), ('retour_presta', 'Retour Presta'), ('en_attente', 'En attente')], string='Etape')
    destinataires = fields.Char(string='Destinataires')
    destinataires_besoin_smartphone = fields.Char(string='Destinataires Smartphones')
    besoin_smartphone = fields.Boolean(string='Besoin Smartphone')

class HelpdeskTicketInherit(models.Model):
    _inherit = 'helpdesk.ticket'

    # Formulaire IT
    status = fields.Char(compute="get_status")
    equipe = fields.Char(compute="get_equipe")

    @api.depends('stage_id')
    def get_status(self):
        self.status = str(self.stage_id.etape)

    @api.depends('team_id')
    def get_equipe(self):
        self.equipe = str(self.team_id.equipe)

    employee_id = fields.Many2one('hr.employee', string='Employé')
    site_rattachment = fields.Selection([('lisses', 'Lisses'),
                                         ('paris', 'Paris'),
                                         ('montaigu', 'Montaigu'), ('bourgoin', 'Bourgoin'),
                                         ('castelnau', 'Castelnau')
                                         ], string='Site de rattachment')

    employee_id = fields.Many2one('hr.employee', string='Employé')
    site_rattachment = fields.Selection([('lisses', 'Lisses'),
                                         ('paris', 'Paris'),
                                         ('montaigu', 'Montaigu'), ('bourgoin', 'Bourgoin'),
                                         ('castelnau', 'Castelnau')
                                         ], string='Site de rattachment')


    question = fields.Selection([
        ('materiel', 'Matèriel'),
        ('logiciel', 'Logiciel'),
        ('master_data', 'Master data')
    ], string='Question concerne')

    materiel = fields.Selection([('pc', 'PC'),
                                 ('smartphone', 'Smartphone'),
                                 ('ipad', 'IPad'), ('imprimante', 'Imprimante'),
                                 ('wap_logistique', 'Wap logistique'),
                                 ('autres', 'Autres')
                                 ], string='Matèriel', required=True)

    logiciel = fields.Selection([('sap', 'SAP'),
                                 ('nomad', 'Nomad'),
                                 ('office', 'Office (teams, outlook)'), ('start', 'Start'),
                                 ('argu', 'L argu au bout des doigts'),
                                 ('ecommerce', 'Site E-commerce'),
                                 ('cleemy', 'Cleemy/Timmy'), ('note_frais', 'Note de frais/Congés'),
                                 ('kyriba', 'Kyriba'), ('wechek', 'Wechek'), ('vim', 'VIM'),
                                 ], string='Logiciel', required=True)

    sujet = fields.Char(string='Sujet', required=True)
    sujet_master_data = fields.Char(string='Sujet', required=True)

    seul_impacte = fields.Selection([('oui', 'Oui'),
                                     ('non', 'Non'),

                                     ], string='Seul impacté', default='oui', required=True)

    travaille = fields.Selection([('oui', 'Oui'),
                                  ('non', 'Non'),

                                  ], string='Continuation de travailler', default='oui', required=True)

    num_transaction = fields.Char(string='Numéro de transaction', required=True)
    num_imprimante = fields.Char(string='Numéro Imprimane', required=True)

    nouveau_materiel = fields.Selection([('oui', 'Oui'),
                                         ('non', 'Non'),

                                         ], string='Demande de nouveau matèriel', default='non', required=True)

    responsable_hierarchique = fields.Char(string='Responsable hierarchique', required=True)

    type_materiel = fields.Selection([('pc', 'PC'),
                                      ('smartphone', 'Smartphone'),
                                      ('ipad', 'Tablette (IPad)'), ('imprimante', 'Imprimante'),
                                      ('ecran', 'Ecran'), ('hub', 'HUB(station)'), ('cable', 'Câble'),
                                      ('autres', 'Autres'),
                                      ], string='Type matèriel', required=True)

    comment = fields.Text(string='Commentaire', required=True)
    comment_master_data = fields.Text(string='Commentaire', required=True)
    piece = fields.Binary(string='Pièce jointe', required=True)
    piece_master_data = fields.Binary(string='Pièce jointe', required=True)

    type_master_data = fields.Selection([('creation', 'Création'),
                                         ('modification', 'Modification'),
                                         ('erreur', 'Erreur'),
                                         ], string='Type', required=True)

    seul_impacte_master_data = fields.Selection([('oui', 'Oui'),
                                                 ('non', 'Non'),

                                                 ], string='Seul impacté', default='oui', required=True)

    # Formulaire RH

    collaborateur = fields.Many2one('hr.employee', string='Employé', required=True)

    pc_housse = fields.Selection([('oui', 'Oui'),
                                  ('non', 'Non'),

                                  ], string='PC + Housse', default='non')
    clavier_souris = fields.Selection([('oui', 'Oui'),
                                       ('non', 'Non'),

                                       ], string='Clavier + Souris Supplémentaire', default='non')

    tablette_chargeur_housse_clavier = fields.Selection([('oui', 'Oui'),
                                                         ('non', 'Non'),

                                                         ], string='Tablette + Chargeur + Housse + Clavier',
                                                        default='non')

    logiciel_commerce = fields.Selection([('nomad', 'Nompad'),
                                          ('start', 'Start'),

                                          ], string='Logiciel Commerce')

    logiciel_finance = fields.Selection([('etafi', 'Etafi (laisse fiscale)'),
                                         ('kyriba', 'Kyriba'), ('wecheck', 'Wecheck'),

                                         ], string='Logiciel Finance')

    logiciel_conge = fields.Selection([('utilisateur', 'Utilisateur'),
                                         ('controlleur', 'Contrôlleur'), ('manager', 'Manager'),
                                         ('admin', 'Admin')
                                         ], string='Logiciel congés et note de frais', default='utilisateur')

    logiciel_paye = fields.Selection([('utilisateur', 'Utilisateur'),
                                       ('controlleur', 'Contrôlleur'), ('manager', 'Manager'),
                                       ('admin', 'Admin')
                                       ], string='Logiciel paye', default='utilisateur')

    logiciel_sap = fields.Selection([('oui', 'Oui'),
                                  ('non', 'Non'),

                                  ], string='Logiciel SAP', default='non')

    nom = fields.Char(string='Nom')

    logiciel_sap_analytic = fields.Selection([('oui', 'Oui'),
                                     ('non', 'Non'),

                                     ], string='Logiciel SAP Analytics', default='non')
    justification = fields.Char(string='Justification d accées')
    vehicule = fields.Selection([('nouveau', 'Nouvea véhicule'),
                                       ('reprise', 'Reprise de véhicule d un Collaborateur'), ('aucun', 'Aucun'),
                                       ('admin', 'Admin')
                                           ], string='Voiture de fonction', default='aucun')
    personne_vehicule = fields.Char(string='nom dont Véhicule')
    acces_dossier = fields.Selection([('oui', 'Oui'),
                                              ('non', 'Non'),

                                              ], string='Accés au dossiers du réseau Supergroupe', default='non')
    nom_reseau = fields.Char(string='Nom des réseaux')
    besoin_imprimante = fields.Selection([('oui', 'Oui'),
                                      ('non', 'Non'),

                                      ], string='Besoin imprimante', default='non')

    besoin_epi = fields.Selection([('oui', 'Oui'),
                                          ('non', 'Non'),

                                          ], string='Besoin en EPI', default='non')

    comment_manager = fields.Text(string='Commentaire de manager')

    def write(self, values):
        res = super(HelpdeskTicketInherit, self).write(values)

        if 'stage_id' in values:

            destinataires = self.stage_id.destinataires

            if self.stage_id.etape == 'traitement_prestataire':
                if self.stage_id.besoin_smartphone == True:
                    if self.stage_id.destinataires:
                        if self.stage_id.destinataires_besoin_smartphone:
                            destinataires = str(self.stage_id.destinataires) + ',' + str(
                                self.stage_id.destinataires_besoin_smartphone)

                    if self.stage_id.destinataires_besoin_smartphone:
                        if self.stage_id.destinataires:
                            destinataires = str(self.stage_id.destinataires) + ',' + str(
                                self.stage_id.destinataires_besoin_smartphone)
                        else:
                            destinataires = str(self.stage_id.destinataires_besoin_smartphone)

                mail_template = self.env.ref('custom_helpdesk.email_template_traitement_prestataire')

                # mail_context = {
                #
                #     'email_from': 'omar@exploit-consult.com',
                #     'email_to': 'exploitconsult2022@gmail.com',
                #
                # }

                mail_context = {

                    'email_to': destinataires,

                }

                mail_template.sudo().send_mail(self.id, email_values=mail_context, force_send=True)




            elif self.stage_id.etape == 'preparation_coordinateur_it':
                # _logger.info('*************** preparation_coordinateur_it %s', self.stage_id.etape)
                mail_template = self.env.ref('custom_helpdesk.email_template_coordinateur_it')

                mail_context = {

                    'email_to': destinataires,

                }

                mail_template.sudo().send_mail(self.id, email_values=mail_context, force_send=True)



            elif self.stage_id.etape == 'traitement_manager':
                # _logger.info('*************** email_template_bylink %s', self.stage_id.etape)
                mail_template = self.env.ref('custom_helpdesk.email_template_traitement_manager')

                mail_context = {

                    'email_to': destinataires,

                }

                mail_template.sudo().send_mail(self.id, email_values=mail_context, force_send=True)

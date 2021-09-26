from odoo import models, fields

class SubscribeUser(models.Model):
    _name = 'subscribe.user'

    email = fields.Char(string="Email")
    state = fields.Selection(string="State", selection=[('req', 'Requested'), ('res', 'Responsed'), ])
    product_id = fields.Many2one(comodel_name="product.template", string="Product")

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    subscribe_user_ids = fields.One2many(comodel_name="subscribe.user", inverse_name="product_id", string="Subscribe User")

    def action_send_mail(self):
        if self.subscribe_user_ids:
            users = self.env['subscribe.user'].search([('product_id','=',self.id),('state','=','req')])
            if users:
                for user in users:
                    if user.email:
                        template = self.env.ref('website_product_subscription.subscribe_product_to_users')
                        template.send_mail(
                            self.id, force_send=True, email_values={"email_to": user.email}
                        )
                        user.state = 'res'


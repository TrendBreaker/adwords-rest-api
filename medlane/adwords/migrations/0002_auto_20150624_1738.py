# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('adwords', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account',
            field=models.CharField(help_text='Account descriptive name', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='currency',
            field=models.CharField(help_text='Account currency code', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='status',
            field=models.CharField(default='active', max_length=32, choices=[('active', 'Active'), ('sync', 'Sync'), ('inactive', 'Inactive')]),
        ),
        migrations.AlterField(
            model_name='ad',
            name='ad',
            field=models.TextField(help_text='Ad/Headline', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='ad_approval_status',
            field=models.CharField(blank=True, null=True, max_length=20, choices=[('approved', 'Approved'), ('approved (non family)', 'Approved (Non Family)'), ('approved (adult)', 'Approved (Adult)'), ('pending review', 'Pending Review'), ('disapproved', 'Disapproved')]),
        ),
        migrations.AlterField(
            model_name='ad',
            name='ad_id',
            field=models.BigIntegerField(help_text='Googles Ad ID'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='ad_state',
            field=models.CharField(blank=True, null=True, max_length=20, choices=[('enabled', 'Enabled'), ('paused', 'Paused'), ('removed', 'Removed')]),
        ),
        migrations.AlterField(
            model_name='ad',
            name='ad_type',
            field=models.CharField(blank=True, null=True, max_length=20, choices=[('Other', 'Other'), ('Image ad', 'Image Ad'), ('Mobile ad', 'Mobile Ad'), ('Product listing ad', 'Product Listing Ad'), ('Display ad', 'Display Ad'), ('Text ad', 'Text Ad'), ('Third party ad', 'Third Party Ad'), ('Dynamic search ad', 'Dynamic Search Ad')]),
        ),
        migrations.AlterField(
            model_name='ad',
            name='description_line_1',
            field=models.TextField(help_text='Description line 1', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='description_line_2',
            field=models.TextField(help_text='Description line 2', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='destination_url',
            field=models.TextField(help_text='Destination URL', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='display_url',
            field=models.TextField(help_text='Display URL', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='adgroup',
            name='ad_group',
            field=models.CharField(help_text='Ad group name', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='adgroup',
            name='ad_group_state',
            field=models.CharField(blank=True, null=True, max_length=20, choices=[('enabled', 'Enabled'), ('paused', 'Paused'), ('removed', 'Removed')]),
        ),
        migrations.AlterField(
            model_name='alert',
            name='severity',
            field=models.CharField(max_length=100, choices=[('GREEN', 'Green'), ('YELLOW', 'Yellow'), ('RED', 'Red'), ('UNKNOWN', 'Unknown')]),
        ),
        migrations.AlterField(
            model_name='alert',
            name='type',
            field=models.CharField(max_length=100, choices=[('ACCOUNT_ON_TARGET', 'Account On Target'), ('DECLINED_PAYMENT', 'Declined Payment'), ('CREDIT_CARD_EXPIRING', 'Credit Card Expiring'), ('ACCOUNT_BUDGET_ENDING', 'Account Budget Ending'), ('CAMPAIGN_ENDING', 'Campaign Ending'), ('PAYMENT_NOT_ENTERED', 'Payment Not Entered'), ('MISSING_BANK_REFERENCE_NUMBER', 'Missing Bank Reference Number'), ('CAMPAIGN_ENDED', 'Campaign Ended'), ('ACCOUNT_BUDGET_BURN_RATE', 'Account Budget Burn Rate'), ('USER_INVITE_PENDING', 'User Invite Pending'), ('USER_INVITE_ACCEPTED', 'User Invite Accepted'), ('MANAGER_LINK_PENDING', 'Manager Link Pending'), ('ZERO_DAILY_SPENDING_LIMIT', 'Zero Daily Spending Limit'), ('TV_ACCOUNT_ON_TARGET', 'TV Account On Target'), ('TV_ACCOUNT_BUDGET_ENDING', 'TV Account Budget Ending'), ('TV_ZERO_DAILY_SPENDING_LIMIT', 'TV Zero Daily Spending Limit'), ('UNKNOWN', 'Unknown')]),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='budget',
            field=djmoney.models.fields.MoneyField(help_text='Budget', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='campaign',
            field=models.CharField(help_text='Campaign name', max_length=255),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='campaign_state',
            field=models.CharField(max_length=20, choices=[('enabled', 'Enabled'), ('paused', 'Paused'), ('removed', 'Removed')]),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='avg_cpc',
            field=djmoney.models.fields.MoneyField(help_text='Avg. CPC', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='avg_cpm',
            field=djmoney.models.fields.MoneyField(help_text='Avg. CPM', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='avg_position',
            field=models.DecimalField(help_text='Avg. position', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='click_conversion_rate',
            field=models.DecimalField(help_text='Click conversion rate', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='clicks',
            field=models.IntegerField(help_text='Clicks', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='content_impr_share',
            field=models.DecimalField(help_text='Content Impr. share', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='content_lost_is_budget',
            field=models.DecimalField(help_text='Content Lost IS (budget)', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='content_lost_is_rank',
            field=models.DecimalField(help_text='Content Lost IS (rank)', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='conv_rate',
            field=models.DecimalField(help_text='Conv. rate', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='conversions',
            field=models.BigIntegerField(help_text='Conversions', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='converted_clicks',
            field=models.BigIntegerField(help_text='Converted clicks', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='cost',
            field=djmoney.models.fields.MoneyField(help_text='Cost', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='cost_conv',
            field=djmoney.models.fields.MoneyField(help_text='Cost / conv.', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='cost_converted_click',
            field=djmoney.models.fields.MoneyField(help_text='Cost / converted click', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='cost_est_total_conv',
            field=djmoney.models.fields.MoneyField(help_text='Cost / est. total conv.', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='ctr',
            field=models.DecimalField(help_text='CTR', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='day',
            field=models.DateField(help_text='When this metric occurred'),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='device',
            field=models.CharField(help_text='Device', max_length=255, choices=[('Other', 'Other'), ('Computers', 'Computers'), ('Mobile devices with full browsers', 'Mobile devices with full browsers'), ('Tablets with full browsers', 'Tablets with full browsers')]),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='est_cross_device_conv',
            field=models.BigIntegerField(help_text='Est. cross-device conv.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='est_total_conv',
            field=models.BigIntegerField(help_text='Est. total conv.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='est_total_conv_rate',
            field=models.DecimalField(help_text='Est. total conv. rate', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='est_total_conv_value',
            field=models.DecimalField(help_text='Est. total conv. value', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='est_total_conv_value_click',
            field=models.DecimalField(help_text='Est. total conv. value / click', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='est_total_conv_value_cost',
            field=models.DecimalField(help_text='Est. total conv. value / cost', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='impressions',
            field=models.BigIntegerField(help_text='Impressions', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='invalid_click_rate',
            field=models.DecimalField(help_text='Invalid click rate', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='invalid_clicks',
            field=models.BigIntegerField(help_text='Invalid clicks', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='search_exact_match_is',
            field=models.DecimalField(help_text='Search Exact match IS', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='search_impr_share',
            field=models.DecimalField(help_text='Search Impr. share', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='search_lost_is_budget',
            field=models.DecimalField(help_text='Search Lost IS (budget)', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='search_lost_is_rank',
            field=models.DecimalField(help_text='Search Lost IS (rank)', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyaccountmetrics',
            name='total_conv_value',
            field=models.DecimalField(help_text='Total conv. value', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='avg_cpc',
            field=djmoney.models.fields.MoneyField(help_text='Avg. CPC', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='avg_cpm',
            field=djmoney.models.fields.MoneyField(help_text='Avg. CPM', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='avg_position',
            field=models.DecimalField(help_text='Avg. position', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='bid_strategy_id',
            field=models.BigIntegerField(help_text='Bid Strategy ID', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='bid_strategy_type',
            field=models.CharField(help_text='Bid Strategy Type', blank=True, null=True, max_length=40, choices=[('auto', 'Budget Optimizer'), ('max/target cpa', 'Conversion Optimizer'), ('cpc', 'Manual CPC'), ('cpm', 'Manual CPM'), ('Target search page location', 'Page One Promoted'), ('max cpa percent', 'Percent CPA'), ('Maximize clicks', 'Target Spend'), ('Enhanced CPC', 'Enhanced CPC'), ('Target CPA', 'Target CPA'), ('Target ROAS', 'Target ROAS'), ('None', 'None'), ('unknown', 'Unknown')]),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='click_conversion_rate',
            field=models.DecimalField(help_text='Click conversion rate', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='clicks',
            field=models.IntegerField(help_text='Clicks', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='content_impr_share',
            field=models.DecimalField(help_text='Content Impr. share', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='content_lost_is_rank',
            field=models.DecimalField(help_text='Content Lost IS (rank)', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='conv_rate',
            field=models.DecimalField(help_text='Conv. rate', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='conversions',
            field=models.BigIntegerField(help_text='Conversions', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='converted_clicks',
            field=models.BigIntegerField(help_text='Converted clicks', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='cost',
            field=djmoney.models.fields.MoneyField(help_text='Cost', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='cost_conv',
            field=djmoney.models.fields.MoneyField(help_text='Cost / conv.', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='cost_converted_click',
            field=djmoney.models.fields.MoneyField(help_text='Cost / converted click', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='cost_est_total_conv',
            field=djmoney.models.fields.MoneyField(help_text='Cost / est. total conv.', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='ctr',
            field=models.DecimalField(help_text='CTR', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='day',
            field=models.DateField(help_text='When this metric occurred'),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='est_cross_device_conv',
            field=models.BigIntegerField(help_text='Est. cross-device conv.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='est_total_conv',
            field=models.BigIntegerField(help_text='Est. total conv.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='est_total_conv_rate',
            field=models.DecimalField(help_text='Est. total conv. rate', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='est_total_conv_value',
            field=models.DecimalField(help_text='Est. total conv. value', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='est_total_conv_value_click',
            field=models.DecimalField(help_text='Est. total conv. value / click', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='est_total_conv_value_cost',
            field=models.DecimalField(help_text='Est. total conv. value / cost', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='impressions',
            field=models.BigIntegerField(help_text='Impressions', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='max_cpa_converted_clicks',
            field=djmoney.models.fields.MoneyField(help_text='Max. CPA (converted clicks)', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='search_exact_match_is',
            field=models.DecimalField(help_text='Search Exact match IS', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='search_impr_share',
            field=models.DecimalField(help_text='Search Impr. share', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='search_lost_is_rank',
            field=models.DecimalField(help_text='Search Lost IS (rank)', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='total_conv_value',
            field=models.DecimalField(help_text='Total conv. value', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='value_conv',
            field=models.DecimalField(help_text='Value / conv.', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='value_converted_click',
            field=models.DecimalField(help_text='Value / converted click', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='value_est_total_conv',
            field=models.DecimalField(help_text='Value / est. total conv.', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadgroupmetrics',
            name='view_through_conv',
            field=models.BigIntegerField(help_text='View-through conv.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='avg_cpc',
            field=djmoney.models.fields.MoneyField(help_text='Avg. CPC', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='avg_cpm',
            field=djmoney.models.fields.MoneyField(help_text='Avg. CPM', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='avg_position',
            field=models.DecimalField(help_text='Avg. position', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='click_conversion_rate',
            field=models.DecimalField(help_text='Click conversion rate', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='clicks',
            field=models.IntegerField(help_text='Clicks', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='conv_rate',
            field=models.DecimalField(help_text='Conv. rate', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='conversions',
            field=models.BigIntegerField(help_text='Conversions', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='converted_clicks',
            field=models.BigIntegerField(help_text='Converted clicks', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='cost',
            field=djmoney.models.fields.MoneyField(help_text='Cost', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='cost_conv',
            field=djmoney.models.fields.MoneyField(help_text='Cost / conv.', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='cost_converted_click',
            field=djmoney.models.fields.MoneyField(help_text='Cost / converted click', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='ctr',
            field=models.DecimalField(help_text='CTR', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='day',
            field=models.DateField(help_text='When this metric occurred'),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='impressions',
            field=models.BigIntegerField(help_text='Impressions', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='total_conv_value',
            field=models.DecimalField(help_text='Total conv. value', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='value_conv',
            field=models.DecimalField(help_text='Value / conv.', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='value_converted_click',
            field=models.DecimalField(help_text='Value / converted click', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailyadmetrics',
            name='view_through_conv',
            field=models.BigIntegerField(help_text='View-through conv.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='avg_cpc',
            field=djmoney.models.fields.MoneyField(help_text='Avg. CPC', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='avg_cpm',
            field=djmoney.models.fields.MoneyField(help_text='Avg. CPM', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='avg_position',
            field=models.DecimalField(help_text='Avg. position', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='bid_strategy_id',
            field=models.BigIntegerField(help_text='Bid Strategy ID', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='bid_strategy_type',
            field=models.CharField(help_text='Bid Strategy Type', blank=True, null=True, max_length=40, choices=[('auto', 'Budget Optimizer'), ('max/target cpa', 'Conversion Optimizer'), ('cpc', 'Manual CPC'), ('cpm', 'Manual CPM'), ('Target search page location', 'Page One Promoted'), ('max cpa percent', 'Percent CPA'), ('Maximize clicks', 'Target Spend'), ('Enhanced CPC', 'Enhanced CPC'), ('Target CPA', 'Target CPA'), ('Target ROAS', 'Target ROAS'), ('None', 'None'), ('unknown', 'Unknown')]),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='click_conversion_rate',
            field=models.DecimalField(help_text='Click conversion rate', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='clicks',
            field=models.IntegerField(help_text='Clicks', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='content_impr_share',
            field=models.DecimalField(help_text='Content Impr. share', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='content_lost_is_budget',
            field=models.DecimalField(help_text='Content Lost IS (budget)', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='content_lost_is_rank',
            field=models.DecimalField(help_text='Content Lost IS (rank)', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='conv_rate',
            field=models.DecimalField(help_text='Conv. rate', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='conversions',
            field=models.BigIntegerField(help_text='Conversions', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='converted_clicks',
            field=models.BigIntegerField(help_text='Converted clicks', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='cost',
            field=djmoney.models.fields.MoneyField(help_text='Cost', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='cost_conv',
            field=djmoney.models.fields.MoneyField(help_text='Cost / conv.', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='cost_converted_click',
            field=djmoney.models.fields.MoneyField(help_text='Cost / converted click', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='cost_est_total_conv',
            field=djmoney.models.fields.MoneyField(help_text='Cost / est. total conv.', default=Decimal('0'), decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='ctr',
            field=models.DecimalField(help_text='CTR', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='day',
            field=models.DateField(help_text='When this metric occurred'),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='est_cross_device_conv',
            field=models.BigIntegerField(help_text='Est. cross-device conv.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='est_total_conv',
            field=models.BigIntegerField(help_text='Est. total conv.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='est_total_conv_rate',
            field=models.DecimalField(help_text='Est. total conv. rate', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='est_total_conv_value',
            field=models.DecimalField(help_text='Est. total conv. value', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='est_total_conv_value_click',
            field=models.DecimalField(help_text='Est. total conv. value / click', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='est_total_conv_value_cost',
            field=models.DecimalField(help_text='Est. total conv. value / cost', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='impressions',
            field=models.BigIntegerField(help_text='Impressions', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='invalid_click_rate',
            field=models.DecimalField(help_text='Invalid click rate', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='invalid_clicks',
            field=models.BigIntegerField(help_text='Invalid clicks', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='search_exact_match_is',
            field=models.DecimalField(help_text='Search Exact match IS', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='search_impr_share',
            field=models.DecimalField(help_text='Search Impr. share', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='search_lost_is_budget',
            field=models.DecimalField(help_text='Search Lost IS (budget)', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='search_lost_is_rank',
            field=models.DecimalField(help_text='Search Lost IS (rank)', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='total_conv_value',
            field=models.DecimalField(help_text='Total conv. value', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='value_conv',
            field=models.DecimalField(help_text='Value / conv.', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='value_converted_click',
            field=models.DecimalField(help_text='Value / converted click', decimal_places=2, max_digits=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dailycampaignmetrics',
            name='view_through_conv',
            field=models.BigIntegerField(help_text='View-through conv.', null=True, blank=True),
        ),
    ]

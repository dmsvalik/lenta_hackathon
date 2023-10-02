def to_representation(self, instance):
        data = super().to_representation(instance)
        data['store'] = data['store']['store']  # Получите значение 'store' из вложенного сериализатора
        data['sku'] = data['sku']['sku']

        # data['fact'] = [{'date': fact_instance['date'],
        #                  'sales_type': fact_instance['sales_type'],
        #                  'sales_units': fact_instance['sales_units'],
        #                  'sales_units_promo': fact_instance['sales_units_promo'],
        #                  'sales_rub': fact_instance['sales_rub'],
        #                  'sales_run_promo': fact_instance['sales_run_promo']}
        #                 for fact_instance in data['fact']]
        
        # data['fact'] = [{'date': fact_instance.date,
        #                  'sales_type': fact_instance.sales_type,
        #                  'sales_units': fact_instance.sales_units,
        #                  'sales_units_promo': fact_instance.sales_units_promo,
        #                  'sales_rub': fact_instance.sales_rub,
        #                  'sales_run_promo': fact_instance.sales_run_promo}
        #                 for fact_instance in instance.fact.all()]
        return data
    
    
    # def to_representation(self, instance):
    #     # Переопределение представления для вложенного сериализатора
    #     return instance.store
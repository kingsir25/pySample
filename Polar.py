from pyecharts import Polar

radius = ['案件1', '案件2', '案件3', '案件4', '案件5', '案件6', '案件7']
polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
polar.add("HLE", [1, 2, 3, 4, 3, 5, 1], radius_data=radius,
          type='barRadius', is_stack=True)
polar.add("Build", [2, 4, 6, 1, 2, 3, 1], radius_data=radius,
          type='barRadius', is_stack=True)
polar.add("ST", [1, 2, 3, 4, 1, 2, 5], radius_data=radius,
          type='barRadius', is_stack=True)
polar.render()
def order_by_far(solider_list):
    # solider=create_solider(solider_list)
    solider_list.sort(key=lambda solider:solider.far_from_base, reverse=True)
    return solider_list
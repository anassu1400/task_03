from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	'my_list': [
    			{
    				"resaurant_name": "Mcdonald's",
    				"food_type": "Fast Food",
    			},
    			{
    				"resaurant_name": "Herfy",
    				"food_type": "Fast Food",
    			},
    			{
    				"resaurant_name": "Kudu",
    				"food_type": "Fast Food",
    			},
    			{
    				"resaurant_name": "Hardee's",
    				"food_type": "Fast Food",
    			},

    	]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	'my_object': {
    		"resaurant_name": "Kudu",
    		"food_type": "Fast Food",
    	},
    }
    return render(request, 'detail.html', context)

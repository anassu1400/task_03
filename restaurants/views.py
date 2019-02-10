from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	'my_list': [
    			{
    				"restaurant_name": "Mcdonald's",
    				"food_type": "Fast Food",
    			},
    			{
    				"restaurant_name": "Herfy",
    				"food_type": "Fast Food",
    			},
    			{
    				"restaurant_name": "Kudu",
    				"food_type": "Fast Food",
    			},
    			{
    				"restaurant_name": "Hardee's",
    				"food_type": "Fast Food",
    			},

    	]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	'my_object': {
    		"restaurant_name": "Kudu",
    		"food_type": "Fast Food",
    	},
    }
    return render(request, 'detail.html', context)

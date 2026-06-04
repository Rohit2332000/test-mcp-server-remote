from fastmcp import FastMCP
import random
import json


#create the mcp server instance
mcp=FastMCP(name='Simple Calculator Server')

#TOOl:add two numbers
@mcp.tool
def add(a:float, b:float )->float:
    """  
    Add two numbers together.
    Args:
        a:first number
        b:second number
        
    Returns:
        The sum of a and b
    """
    return a + b

#Tool :generate the random numbers
@mcp.tool
def random_number(min_value:int=1,max_value:int=100)->int:
    """Generate a random number between given range
    Args:
        min_value:Minimum Value(default:1)
        max_value:Maximum Value(default:100)
    Returns:
        A random number between min value and max value    
        """
        
    return random.randint(min_value,max_value)

#Resourse:Server information

@mcp.resource('info://server')
def server_info()->str:
    """Get info about this server"""
    info={
        'name':'Simple calculator server',
        'version':'1.0.0',
        'description':'A basic mcp server with tools',
        'tools':['add two numbers','generate random numbers'],
        'developer':'Rohit'
        
    }
    
    return json.dumps(info,indent=2)

#Start the server
if __name__=='__main__':
    mcp.run(transport='http',host='0.0.0.0',port=8000)
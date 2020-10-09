class Object:
    
    def __repr__(self):
        
        return '<%s>' % getattr(self, '__name__', self.__class__.__name__)


    def is_alive(self):


        return hasattr(self, 'alive') and self.alive

    
    def display(self, canvas, x, y, width, height):
        
        pass

class Agent(Object):
    
    def __init__(self):

        def program(percept):

            return raw_input('Percept=%s; action? ' % percept)

        self.program = program

        self.alive = True

class TableDrivenAgent(Agent):

    
    def __init__(self, table):
        
        Agent.__init__(self)
        percepts = []

        def program(percept):
            
            percepts.append(percept)

            action = table.get(tuple(percepts))

            return action

        self.program = program


class ReflexVacuumAgent(Agent):

    
    def __init__(self):

        Agent.__init__(self)
        
        def program(status):

            if status == 'Hi': return 'Hello'

            elif status == 'Name': return 'your name or mine '

            elif status == 'your name': return 'I am chatbot'

            elif status == 'my name': return 'jyoti pandey'

            elif status == 'how is the weather': return ' weather is very cold!!!!'

            elif status == 'how are you': return 'i am perfectly okay'

            elif status == ' how is temp': return 'it is normal'

            elif status == 'who is the pm of india': return 'narendra modi'

            elif status == 'country': return 'India'

            elif ststus=='song':return'tum hi aana'

        self.program = program


def TableDrivenVacuumAgent():

    table = {((A, 'Hey'),): 'Hello, I am Chatbot',

             ((A, 'Hello'),): 'Hello, I am Chatbot',

             ((A, 'Hey, how are you'),): 'Hello, I am perfectly okay',
             ((A, 'Name'),): 'my name or yours?',
             ((A, 'Your name'),): 'I am Chatbot',
             ((A, 'my name'),): 'jyoti pandey',
            
             ((A, 'how is temp'),): 'it is normal',
             ((A, 'who is the pm of india'),): 'narendra modi?',
             ((A, ' how is the weather'),): ' weather is very cold',
             ((A, 'country'),): 'India',
             
             ((A, 'song'), (A, 'fabourite')): 'tum hi aana ',
             ((A, 'song'), (A, 'hindi')): 'a lot of hindi song ',
             
                     }

    return TableDrivenAgent(table)


class Environment:

    
    def __init__(self,):

        self.objects = []; self.agents = []



    object_classes = [] ## List of classes that can go into environment



    def percept(self, agent):

        query = input('enter query>')
        return self.execute_action(agent,query)
        
    def execute_action(self, agent, query):

        return agent.program(query)


if __name__ == "__main__":

    e1 = Environment()
    rAgent = ReflexVacuumAgent()
    print(e1.percept(rAgent))





in_state = input("input a state to get the capital:  ")
state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                       'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                       'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}

result = state_dictionary.get(in_state.title(), "unknown capital")
print(result)
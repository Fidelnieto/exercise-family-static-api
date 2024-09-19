
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1

        # example list of members
        self._members = [
        {
         "id": self._next_id,
         "first_name": "John",
         "last_name": self.last_name,
         "age": 33 ,
         "lucky_numbers": [7, 13, 22],
        },
        {
         "id": self._next_id + 1,
         "first_name": "Jane",
         "last_name": self.last_name,
         "age": 35 ,
         "lucky_numbers": [10, 14, 3],
        },
        {
         "id": self._next_id + 2,
         "first_name": "Jimmy",
         "last_name": self.last_name,
         "age": 5,
         "lucky_numbers": [1],
        }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        member['id'] = self._generateId()
        member['last_name'] = self.last_name
        self._members.append(member)
        pass

    def delete_member(self, id):
        selected_member_id = any(member['id'] == id for member in self._members)
        del self._members[selected_member_id]
        pass

    def get_member(self, id):
        selected_member = next((member for member in self._members if member['id'] == id), None)

        return selected_member
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

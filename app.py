from flask import Flask,request
import graphene, json

app = Flask(__name__)

class Query(graphene.ObjectType):
    person = graphene.String(name=graphene.String(default_value="stranger"), age=graphene.Argument(graphene.Int))
    test = graphene.String()
    def resolve_person(self, info, **args):
        return 'Hello {} you are {} years old'.format(args['name'], args['age'])

schema = graphene.Schema(query=Query)

@app.route("/graphql", methods=['POST'])
def graphql():
    data = json.loads(request.data)
    return json.dumps(schema.execute(data['query']).data)

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')
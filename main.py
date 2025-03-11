from flask import Flask, request
from tornado.process import task_id
from tarefa import Tarefa
app = Flask(__name__)
tarefas = [
    Tarefa(task_id=1, titulo="Estudar Js", descricao="Estudar Js para aprender  a construir eventos nas páginas web", status="Em andamento", dt_inicio="21/02/2025", comentarios="Essa tarefa é importante para fazer bons sites no futuro", dificuldade="média",).to_json(),
    Tarefa(task_id=2, titulo="Estudar Flask", descricao="Estudar Flask para aprender sobre Web Services", status="Não iniciada", dt_inicio="20/02/2025", comentarios="Essa tarefa é importante para fazer bons sites no futuro", dificuldade="alta").to_json(),
    Tarefa(task_id=3, titulo="Iceberg", descricao="Continuar a fazer o Iceberg de Undertale", status="Em andamento", dt_inicio="20/09/2024", comentarios="Essa tarefa é um importante projeto pessoal", dificuldade="baixa").to_json()
]
@app.route('/')
def index():
    return "haljkshalkhskjah"
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return tarefas
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('task_id') == task_id:
            return tarefa
    return 'Tarefa não encontrada'
@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('task_id') + 1
    task['task_id'] = ultimo_id
    tarefas.append(task)
    return task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None
    for tarefa in tarefas:
        if tarefa.get('task_id') == task_id:
            task_search = tarefa
    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')
    task_search['dt_inicio'] = task_body.get('dt_inicio')
    task_search['comentarios'] = task_body.get('comentarios')
    task_search['dificuldade'] = task_body.get('dificuldade')
    return task_search
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for tarefa in tarefas:
        if tarefa.get('task_id') == task_id:
            tarefas.remove(tarefa)
            return {'message': f'Tarefa com id {task_id} foi removida com sucesso.'}
    return {'message': f'Tarefa com id {task_id} não encontrada.'}
if __name__ == '__main__':
    app.run(debug=True)
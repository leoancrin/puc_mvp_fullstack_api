from flask import request, jsonify
from modelos.itens_colecionaveis import ItensColecionaveis
from modelos.tipos_item import TipoItemColecionavel

from extensions import db

# Funções gerais
def valida_tipo_texto(texto):
    if not texto:
        return jsonify({"Erro":"Tipo é obrigatório"}), 400

def metodo_cadastrar_tipos():
    dados = request.get_json()

    tipo_requisicao = dados.get("tipo_item")

    valida_tipo_texto(tipo_requisicao) 

    try:
        tipo_cadastrado = TipoItemColecionavel(
            tipo_item = dados.get("tipo_item")
        )

        select_tipo_pelo_nome = db.select(TipoItemColecionavel).filter_by(tipo_item=tipo_requisicao)

        tipo_existente = db.session.execute(select_tipo_pelo_nome).scalar_one_or_none()
        if tipo_existente:
            return jsonify({"Erro":"Tipo já cadastrado"}), 400

        db.session.add(tipo_cadastrado)
        db.session.commit()

        return jsonify({"mensagem":"Tipo cadastrado com sucesso"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"Erro ao cadastrar tipo": str(e)}), 400

def metodo_consultar_tipos():
    try:
        select_todos_tipos = db.select(TipoItemColecionavel).order_by(TipoItemColecionavel.id_tipo)
        tipos_itens = db.session.execute(select_todos_tipos).scalars().all()

        resultado = [
            {"id_tipo": tipo.id_tipo, "tipo_item": tipo.tipo_item}
            for tipo in tipos_itens
        ]
        return jsonify(resultado), 200
    
    except Exception as e:
        return jsonify({"Erro ao recuperar os tipos": str(e)}), 400

def metodo_alterar_tipos():
    dados = request.get_json()
   
    tipo_requisicao = dados.get("tipo_item")
    id_requisicao = dados.get("id_tipo")
   
    valida_tipo_texto(tipo_requisicao) 
   
    try:   
        select_tipo_por_id = db.select(TipoItemColecionavel).filter_by(id_tipo=id_requisicao)   
        tipo_a_alterar = db.session.execute(select_tipo_por_id).scalar_one()

        tipo_a_alterar.tipo_item = tipo_requisicao
           
        db.session.commit()
   
        return jsonify({"mensagem":"Tipo alterado com sucesso"}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"Erro ao alterar tipo": str(e)}), 400 

def metodo_deletar_tipos():
    dados = request.get_json()
      
    tipo_requisicao = dados.get("tipo_item")
    id_requisicao = dados.get("id_tipo")
      
    valida_tipo_texto(tipo_requisicao)

    try:
        select_item_colecionavel = db.select(ItensColecionaveis).filter_by(tipo=id_requisicao)
        tipo_existente_item = db.session.execute(select_item_colecionavel).scalar_one_or_none()

        if tipo_existente_item:
            return jsonify({"Erro ao deletar tipo": "Existe item com esse tipo definido"}), 400

        select_tipo_a_ser_deletado = db.select(TipoItemColecionavel).filter_by(id_tipo=id_requisicao)
        tipo_a_ser_deletado = db.session.execute(select_tipo_a_ser_deletado).scalar_one()

        if tipo_a_ser_deletado.tipo_item != tipo_requisicao:
            return jsonify({"Erro ao deletar tipo": "Verifique se o nome do tipo está correto"}), 400

        db.session.delete(tipo_a_ser_deletado) 
        db.session.commit()

        return jsonify({"mensagem": "Tipo deletado com sucesso"}), 200 

    except Exception as e:
        db.session.rollback()
        return jsonify({"Erro ao deletar tipo": str(e)}), 400 
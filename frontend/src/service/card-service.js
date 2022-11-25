export default class CardService {

  _apiBase = 'http://localhost:8000/api/v1/card';

  getResource = async (url) => {
    const res = await fetch(`${this._apiBase}${url}`)

    if (!res.ok) {
      throw new Error(`Could not fetch ${url}` +
        `, received ${res.status}`)
    }
    return await res.json()
  };

  getAllPersons = async () => {
    const res = await this.getResource(`/persons`);
    return res.map(this._transformPerson)
  };

  _transformPerson = (person) => {
    return {
      id: person.id,
      name: person.name,
    }
  }
  getCard = async (id) => {
    const res = await this.getResource(`/card_person/${id}`);
    return res.map(this._transformCard)
  };

  _transformCard = (card) => {
    return {
      id: card.id,
      skill: card.skill,
      progress: card.progress,
      comment: card.comment,
    }
  }
}

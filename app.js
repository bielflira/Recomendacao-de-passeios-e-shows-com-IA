import { useState } from 'react';
import { View, Text, TextInput, Button, ScrollView } from 'react-native';

export default function App() {

  const [locais, setLocais] = useState("");
  const [musicas, setMusicas] = useState("");
  const [resultado, setResultado] = useState("");

  const buscar = async () => {
    const res = await fetch("http://SEU_IP:5000/recomendar", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ locais, musicas })
    });

    const data = await res.json();
    setResultado(JSON.stringify(data, null, 2));
  };

  return (
    <ScrollView style={{ padding: 20 }}>
      <Text style={{ fontSize: 24 }}>🔥 Rolefy</Text>

      <TextInput placeholder="Locais" onChangeText={setLocais} />
      <TextInput placeholder="Músicas" onChangeText={setMusicas} />

      <Button title="Buscar" onPress={buscar} />

      <Text>{resultado}</Text>
    </ScrollView>
  );
}

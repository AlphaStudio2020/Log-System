# Log System

## Überblick
Das **Log System** ist ein Discord-Bot, der verschiedene Aktionen auf dem Server protokolliert. Dazu gehören Mitgliedsbeitritte, Sprachkanal-Bewegungen, Nachrichten-Interaktionen sowie Rollen- und Moderationsereignisse.

## Funktionen
- Protokollierung von Sprachkanal-Beitritten, -Verlassen und -Wechsel
- Logging von Nachrichtenlöschungen und -bearbeitungen
- Aufzeichnung von Mitgliedsbeitritten und -austritten
- Erfassung von Rollenänderungen
- Protokollierung von Bans, Kicks und Unbans
- Verwendung von `discord.Embed` zur ansprechenden Darstellung der Logs

## Voraussetzungen
- Ein Discord-Bot-Token
- Die `discord.py`-Bibliothek (Async-Version)
- Die ID des Log-Kanals

## Installation
1. Stelle sicher, dass Python (Version 3.8 oder höher) installiert ist.
2. Installiere die `discord.py`-Bibliothek mit folgendem Befehl:
   ```sh
   pip install discord
   ```
3. Füge den Bot zu deinem Discord-Server hinzu und aktiviere `Intents`.

## Einrichtung
1. Ersetze `TOKEN_HIER` in der Datei durch deinen Bot-Token.
2. Setze `LOG_CHANNEL_ID` auf die ID des Log-Kanals.
3. Starte den Bot mit:
   ```sh
   python bot.py
   ```

## Anpassung
- Falls du einen anderen Befehlsprefix verwenden möchtest, ändere `command_prefix="!"` in eine andere Zeichenfolge.
- Du kannst die protokollierten Events anpassen, indem du bestimmte Event-Handler bearbeitest oder hinzufügst.

## Fehlerbehebung
Falls der Bot nicht funktioniert:
- Stelle sicher, dass der Bot die richtigen Berechtigungen hat (z. B. Nachrichten senden, Kanäle verwalten, Mitglieder verwalten).
- Überprüfe, ob die Kanal-IDs und der Bot-Token korrekt sind.
- Falls der Log-Kanal nicht gefunden wird, prüfe, ob die ID richtig gesetzt wurde.

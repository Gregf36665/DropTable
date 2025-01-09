# DropTable

## Usage

```
drop_table.py [-h] inputfile outputfile npcname
```

## Details

[2004Scape](https://github.com/2004Scape/Server) uses .rs2 files, written in runescript to implement drop tables. To find the correct values [RSC](https://classic.runescape.wiki/), [OSRS](https://oldschool.runescape.wiki/w/Old_School_RuneScape_Wiki) and [RS3](https://runescape.wiki/w/RuneScape_Wiki) need to be consulted.

Fortunately they all use the same format for drop tables.
<details>
  <summary>For example </summary>
  
  ```
  ==Drops==
{{Estimated drops}}
===100% drops===
{{DropsTableHead}}
{{DropsLine|Name=Bones|Quantity=1|Rarity=Always}}
{{DropsTableBottom}}

===Weapons and armour===
{{DropsTableHead}}
{{DropsLine|Name=Bronze Spear|Quantity=2|Rarity=4/128}}
{{DropsLine|Name=Bronze Spear|Quantity=1|Rarity=3/128}}
{{DropsLine|Name=Mithril Spear|Quantity=1|Rarity=3/128}}
{{DropsLine|Name=Iron Spear|Quantity=1|Rarity=2/128}}
{{DropsTableBottom}}

===Runes and ammunition===
{{DropsTableHead}}
{{DropsLine|Name=Nature-Rune|Quantity=2|Rarity=8/128}}
{{DropsLine|Name=Poison Bronze Arrows|Quantity=5|Rarity=2/128}}
{{DropsLine|Name=Poison Crossbow bolts|Quantity=4|Rarity=2/128}}
{{DropsTableBottom}}

===Coins===
{{DropsTableHead}}
{{DropsLine|Name=Coins|Quantity=15|Rarity=25/128}}
{{DropsLine|Name=Coins|Quantity=28|Rarity=12/128}}
{{DropsLine|Name=Coins|Quantity=62|Rarity=5/128}}
{{DropsLine|Name=Coins|Quantity=42|Rarity=3/128}}
{{DropsTableBottom}}

===Herbs===
{{DropsTableHead}}
{{HerbDropTable/Sandbox|11/128}}
{{DropsTableBottom}}

===Other===
{{DropsTableHead}}
{{DropsLine|Name=Snape grass|Quantity=1|Rarity=23/128}}
{{DropsLine|Name=Limpwurt root|Quantity=1|Rarity=12/128}}
{{DropsLine|Name=Gold|Quantity=1|Rarity=5/128}}
{{DropsLine|Name=Poison antidote (2 dose)|Quantity=1|Rarity=3/128}}
{{DropsLine|Name=Poison antidote (3 dose)|Quantity=1|Rarity=1/128}}
{{DropsLine|Name=Nothing|Rarity=2/128}}
{{DropsTableBottom}}

===Rare drop table===
{{RareDropTable|RDT=2/128}}

{{Jungle potion}}
{{Tai Bwo Wannai}}
```
</details>

This tool parses this data and converts it to rs2. All you have to do is specify the name of the NPC according to rs2. You can find that in [npc.pack](https://github.com/2004Scape/Server/blob/main/data/src/pack/npc.pack)


If you run into problems please create an [issue](https://github.com/Gregf36665/DropTable/issues/new)

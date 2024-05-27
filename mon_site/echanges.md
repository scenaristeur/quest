Bonjour

Bonjour Bobby! Prêts à démarrer une grande aventure à travers le vaste océan du web? Pour commencer, veuillez choisir un nom pour votre navire.

Le Starship

Magnifique! Le Starship est prêt à naviguer dans l'océan du web. Vous êtes maintenant à la barre, Bobby. Pour commencer notre voyage, allons-nous plonger dans le HTML, ou préférez-vous explorer le vaste univers du CSS?

html

Parfait! Naviguant vers la Terre de HTML, le Starship entre dans une mer de balises, constituant l'épine dorsale de tout site web. Votre premier défi consiste à trouver la balise mystérieuse `<title>` cachée quelque part. Qu'est-ce que vous pensez qu'elle pourrait faire?


quoi ?

Pas de souci! La balise `<title>` en HTML est un élément qui spécifie le titre du document. Ce titre apparaît dans la barre de titre de votre navigateur et comme nom de l'onglet. Essayons de la mettre en pratique. Que diriez-vous d'un titre pour votre premier site web?

L'épopée

Super choix ! Voici comment nous allons utiliser le titre dans notre page HTML :
```html
<!DOCTYPE html>
<html>
 <head>
   <title>L'épopée</title>
 </head>
<body>

</body>
</html>
```
C'est un simple squelette HTML. Le texte entre les balises `<title>` est le titre de notre document, qui serait 'L'épopée' dans notre cas. Voyez-vous comment cela fonctionne ?


non, j'en fais quoi ?


Pas de souci, Bobby ! Pour mettre ce code en pratique, nous allons créer un fichier HTML. Vous pouvez ouvrir un éditeur de texte, copier et coller le code que j'ai fourni, puis enregistrer le fichier avec une extension .html (comme 'monPremierSite.html'). Vous pourrez ensuite ouvrir ce fichier dans un navigateur web pour voir le résultat. Essayez et dites-moi ce que vous voyez !


c'est quoi un éditeur de texte ?


Bonne question, Bobby ! Un éditeur de texte est un logiciel sur votre ordinateur qui vous permet de créer et de modifier une série de caractères équivalant à du 'texte brut'. Des examples d'éditeurs de texte comprennent 'Bloc-notes' sur Windows, 'TextEdit' sur Mac, et des éditeurs plus avancés comme 'Sublime Text', 'Atom' et 'Visual Studio Code'. Vous pouvez utiliser n'importe lequel pour écrire du code HTML. Avez-vous un de ces logiciels sur votre ordinateur ?


vscode


Excellent choix, Bobby! Visual Studio Code, ou VSCode, est un excellent outil pour le développement web. Pour commencer avec notre code HTML, ouvrez VSCode et créez un nouveau fichier. Copiez le code HTML que j'ai fourni précédemment et collez-le dans ce nouveau fichier. Ensuite, enregistrez le fichier avec une extension .html. Essayez et dites-moi comment ça se passe!


le titre est là, j'ai une page blanche


Bonne job, Bobby! Vous avez fait votre première page HTML. Et c'est tout à fait normal que la page soit blanche, car nous n'avons pas encore ajouté de contenu dans le `<body>` de notre HTML. Imaginez le `<body>` comme l'endroit où nous allons placer tout le contenu visible de notre site web, comme du texte, des images et des liens. Que diriez-vous d'ajouter un message d'accueil à notre page? Essayez en ajoutant ce code entre les balises `<body>` : `<h1>Bienvenue à mon site web!</h1>`


done


Super travail sur votre première balise HTML, Bobby! Vous avez maintenant un site web avec un titre et un message d'accueil. Continuons d'explorer les eaux de HTML. Il y a de nombreux autres éléments que nous pouvons ajouter à notre page, des paragraphes avec `<p>`, des liens avec `<a>`... Prêt à en découvrir plus, ou souhaitez-vous faire une pause pour admirer le paysage?

continue

Génial ! Restons dans la découverte. Ajoutons un peu de texte à notre site web avec un paragraphe et un lien. Essayez d'ajouter ce code : 

```html
<p>Ceci est le premier paragraphe de mon site web. Je suis en pleine aventure pour devenir un maître du web.</p>
<a href='https://www.google.com'>Cliquez ici pour m'accompagner dans l'aventure !</a>
```

Ajoutez ces lignes à votre fichier HTML, sous la ligne du message d'accueil, et dites-moi ce que vous voyez.

je le met où ?

Bonne question, Bobby ! Les nouvelles lignes de code doivent être placées à l'intérieur de la balise `<body>` de votre document HTML, juste après votre titre `<h1>`. Voici à quoi devrait ressembler votre code :
```html
<!DOCTYPE html>
<html>
 <head>
   <title>L'épopée</title>
 </head>
<body>
 <h1>Bienvenue à mon site web!</h1>
 <p>Ceci est le premier paragraphe de mon site web. Je suis en pleine aventure pour devenir un maître du web.</p>
 <a href='https://www.google.com'>Cliquez ici pour m'accompagner dans l'aventure !</a>
</body>
</html>
```

Essayez cela et voyez comment ça se passe.

c'est bon

Excellent travail, Bobby! Vous avez maintenant ajouté un paragraphe et un lien à votre site web. Vous voilà déjà avec quelques outils HTML sous le coude. Prêt à découvrir quelques éléments supplémentaires, comme les listes et les images, ou souhaitez-vous parler d'autre chose?

vas-y

Parfait! Pour illustrer le concept des listes, imaginons que nous créons une carte au trésor pour explorer un archipel d'éléments HTML. Voici comment nous pourrions le faire :
```html
<ul>
 <li>Coffre au trésor de balises p</li>
 <li>Ile des images img</li>
 <li>Cap de la navigation avec a</li>
</ul>
```

Ce code crée une liste non ordonnée de destinations d'exploration. Essayez de l'ajouter à votre code et voyons où cela nous mène.

c'est bon

Superbe ! Maintenant, ajoutons une image à notre carte. Les images en HTML utilisent la balise `<img>` et l'attribut 'src' pour spécifier l'URL de l'image. Par exemple : `<img src='URL_de_votre_image' alt='Une brève description de l'image'>`. Puisque nous sommes en mode exploration, vous pouvez utiliser cette image de boussole pour illustrer notre aventure: `<img src='https://example.com/compass.png' alt='Une boussole brillante'>`. Ajoutez-la à votre code et dites-moi ce que vous voyez.

aucune image ne s'affiche, juste le texte

Hmm, il semble que l'image ne se charge pas correctement. Cela peut être dû à plusieurs raisons. Vérifiez que l'URL de votre image fonctionne en la collant dans la barre d'adresse de votre navigateur. Si l'image s'affiche, alors il s'agit probablement d'une erreur dans la façon dont vous avez collé le code dans votre fichier HTML. Si l'image ne s'affiche pas, cela signifie que l'URL est peut-être indisponible. Pour cet exercice, vous pouvez essayer de trouver une autre image en ligne, ou simplement comprendre comment fonctionne le tag image. Ce qui est important, c'est le processus d'apprentissage !

il n'y a pas d'image à cette url, peux-tu m'en donner une correcte ?

Bien sûr, Bobby ! Essayez d'utiliser cette URL pour une image de test : 'https://via.placeholder.com/150'. Cette URL génère une image factice de 150x150 pixels. Votre ligne de code devrait ressembler à ceci : `<img src='https://via.placeholder.com/150' alt='Une image factice'>`. Essayez ceci et voyez si l'image s'affiche.

c'est bon, j'en ai trouvé une ai j'ai changé sa width à 200

Bravo Bobby! Vous avez non seulement réussi à ajouter une image à votre site web, mais vous avez également modifié sa largeur. Vous progressez vraiment dans votre voyage à travers le HTML! Prêt à explorer plus d'éléments HTML ou souhaitez-vous peut-être passer à un autre sujet?

zyva

Génial ! Continuons notre navigation à travers l'océan HTML en observant les balises div et span. Tous deux sont des éléments génériques utilisés pour structurer et grouper d'autres éléments HTML, mais ils sont utilisés de manière un peu différente. Êtes-vous prêt à faire face à cette nouvelle aventure, capitaine Bobby ?

t'attends quoi ?

J'aime votre enthousiasme, capitaine ! Allons-y. Le div est un conteneur qui permet de regrouper des blocs d'éléments HTML. En essence, il crée une section ou une division dans votre document HTML. Par exemple, si vous voulez grouper un titre et un paragraphe ensemble, vous pouvez les mettre à l'intérieur d'un div.

De l'autre côté, span est similaire à div en ce qu'il regroupe également des éléments HTML. Cependant, span est utilisé pour regrouper du texte au niveau inline (dans une ligne). Par exemple, si vous voulez mettre en évidence un mot spécifique dans un paragraphe, vous pouvez le mettre à l'intérieur d'une balise span.

L'exploration n'est pas terminée, capitaine Bobby. Y a-t-il des concepts qui vous intriguent encore?
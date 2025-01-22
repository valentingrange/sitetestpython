const numberOfSections = 1000; // Augmente le nombre de sections pour une page gigantesque
const body = document.body;

for (let i = 4; i <= numberOfSections + 3; i++) {
    const section = document.createElement('div');
    section.classList.add('section');
    
    const title = document.createElement('h2');
    title.classList.add('title');
    title.textContent = `Section ${i}`;
    
    const content = document.createElement('p');
    content.classList.add('content');
    content.textContent = `Ceci est un énorme exemple de contenu. Il y a plusieurs milliers de lignes similaires à celle-ci pour créer une page longue et impressionnante. Vous pouvez imaginer un site avec beaucoup de contenu dynamique, des images, des vidéos et bien plus encore.`;
    
    section.appendChild(title);
    section.appendChild(content);
    body.appendChild(section);
}
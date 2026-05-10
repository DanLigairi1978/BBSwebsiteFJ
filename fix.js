const fs = require('fs');
const path = require('path');

const dir = path.join(__dirname, 'public');
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

for (const file of files) {
    const filePath = path.join(dir, file);
    let content = fs.readFileSync(filePath, 'utf8');

    // 1. Facebook Links
    content = content.replace(/href="#"(.*?)class="fab fa-facebook-f"/g, 'href="https://www.facebook.com/profile.php?id=100014036929391"$1class="fab fa-facebook-f"');

    // 2. WhatsApp links (if any missing the +679 or just 679)
    // Actually the links already use 6799086990. Let's check for any 9086990
    content = content.replace(/wa\.me\/9086990/g, 'wa.me/6799086990');

    // 5. Phone Links
    content = content.replace(/href="tel:9086990"/g, 'href="tel:+6799086990"');

    // 4. File Paths
    content = content.replace(/href="css\/styles\.css"/g, 'href="./css/styles.css"');
    content = content.replace(/src="js\/main\.js"/g, 'src="./js/main.js"');
    content = content.replace(/src="assets\//g, 'src="./assets/');
    
    // Links to HTML pages
    content = content.replace(/href="index\.html"/g, 'href="./index.html"');
    content = content.replace(/href="services\.html"/g, 'href="./services.html"');
    content = content.replace(/href="why-us\.html"/g, 'href="./why-us.html"');
    content = content.replace(/href="resources\.html"/g, 'href="./resources.html"');
    content = content.replace(/href="contact\.html"/g, 'href="./contact.html"');
    
    // Just in case any /css or /js were used
    content = content.replace(/href="\/css\/styles\.css"/g, 'href="./css/styles.css"');
    content = content.replace(/src="\/js\/main\.js"/g, 'src="./js/main.js"');
    content = content.replace(/src="\/assets\//g, 'src="./assets/');
    content = content.replace(/href="\/index\.html"/g, 'href="./index.html"');
    content = content.replace(/href="\/services\.html"/g, 'href="./services.html"');
    content = content.replace(/href="\/why-us\.html"/g, 'href="./why-us.html"');
    content = content.replace(/href="\/resources\.html"/g, 'href="./resources.html"');
    content = content.replace(/href="\/contact\.html"/g, 'href="./contact.html"');

    // 8. Remove any localhost references
    content = content.replace(/http:\/\/localhost:3000\//g, './');
    content = content.replace(/http:\/\/127\.0\.0\.1:3000\//g, './');

    fs.writeFileSync(filePath, content);
}
console.log('Replacements complete');

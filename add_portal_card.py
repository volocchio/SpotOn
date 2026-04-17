import sys

path = "/var/www/apps-portal/index.html"
with open(path, "r") as f:
    html = f.read()

if "spoton.voloaltro.tech" in html:
    print("ALREADY EXISTS")
    sys.exit(0)

card = '''    <a href="https://spoton.voloaltro.tech" class="card" target="_blank">
      <div class="card-icon">\U0001f4b3</div>
      <div class="card-title">SpotOn Rate Calculator</div>
      <div class="card-desc">Compare IC+, Variable, Surcharge and Dual Pricing</div>
    </a>
'''

html = html.replace("</main>", card + "</main>")
with open(path, "w") as f:
    f.write(html)
print("DONE")

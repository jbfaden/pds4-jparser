#!/usr/bin/env python3
from pathlib import Path
import sys

def replace_exact(path, old, new):
    p = Path(path)
    s = p.read_text()
    if old not in s:
        print("ERROR: expected text not found in %s:" % path, file=sys.stderr)
        print(old, file=sys.stderr)
        sys.exit(1)
    s2 = s.replace(old, new, 1)
    p.write_text(s2)
    print("updated", path)

pom = "pom.xml"

replace_exact(pom,
"""      <artifactId>jaxb-impl</artifactId>
      <version>4.0.5</version>""",
"""      <artifactId>jaxb-impl</artifactId>
      <version>2.3.9</version>""")

replace_exact(pom,
"""      <artifactId>jaxb-xjc</artifactId>
      <version>4.0.7</version>""",
"""      <artifactId>jaxb-xjc</artifactId>
      <version>2.3.9</version>""")

replace_exact(pom,
"""      <groupId>jakarta.xml.bind</groupId>
      <artifactId>jakarta.xml.bind-api</artifactId>
      <version>4.0.5</version>""",
"""      <groupId>javax.xml.bind</groupId>
      <artifactId>jaxb-api</artifactId>
      <version>2.3.1</version>""")

replace_exact(pom,
"""      <groupId>jakarta.activation</groupId>
      <artifactId>jakarta.activation-api</artifactId>
      <version>2.1.4</version>""",
"""      <groupId>javax.activation</groupId>
      <artifactId>javax.activation-api</artifactId>
      <version>1.2.0</version>""")

replace_exact(pom,
"""    <maven.compiler.release>17</maven.compiler.release>""",
"""    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>""")

mapper = "src/main/java/gov/nasa/pds/label/jaxb/PDSNamespacePrefixMapper.java"
replace_exact(mapper,
"""import org.glassfish.jaxb.runtime.marshaller.NamespacePrefixMapper;""",
"""import com.sun.xml.bind.marshaller.NamespacePrefixMapper;""")

print()
print("Java 8 compatibility edits applied.")
print("Review with: git diff")

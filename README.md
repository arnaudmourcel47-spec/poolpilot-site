# PoolPilot public site

Static, dependency-free GitHub Pages source, separate from the iOS project. No app source, user records, photos, archives or IPA are included. The site is hosted at `https://arnaudmourcel47-spec.github.io/poolpilot-site/`. Some legal disclosures remain under review; see the legal-notice pages before treating the site as legally complete.

## Pages

| Language | Home | Privacy | Support | Legal notice |
| --- | --- | --- | --- | --- |
| Français | `/` | `/privacy/` | `/support/` | `/legal/` |
| English | `/en/` | `/en/privacy/` | `/en/support/` | `/en/legal/` |
| Español | `/es/` | `/es/privacy/` | `/es/support/` | `/es/legal/` |

The privacy pages started from the three drafts copied from the PoolPilot iOS project on 14 October 2026. They now include the publisher-confirmed EI and micro-entrepreneur status, SIREN and SIRET, postal address, telephone, contact email, effective date and support-email retention period. The original iOS files were not modified. The legal-notice pages explicitly identify the remaining open points.

## Open legal checks

1. Verify the applicable registration register and reference for the supplied SIREN/SIRET. Confirm the actual VAT regime and whether an intra-community VAT number applies; the publisher says he does not charge VAT, which alone does not establish the franchise en base. Confirm whether publishing PoolPilot matches the EI's declared activity.
2. Resolve the GitHub Pages host telephone requirement and confirm which GitHub entity is legally responsible for this Pages site through qualified legal review. The legal pages list GitHub, Inc. and GitHub B.V. as entities named in GitHub's documentation; they do not present GitHub B.V. as the confirmed contractual host. Do not invent a number.
3. Confirm the App Privacy answers for the exact distributed app build and implement the stated support-email retention period. Do not infer that the absence of an analytics SDK proves no data collection by every platform integration.
4. Rebuild the pages and run the checks below after future changes. Read all twelve pages in a browser, including on a narrow screen.

## Local build and preview

```sh
python3 scripts/build.py
python3 scripts/check_site.py
python3 -m http.server 8000
```

Open `http://localhost:8000/` while the server runs. The build uses only Python's standard library; the published pages need no JavaScript, fonts, CDN, analytics or cookies.

## Updating the existing public site

1. Review the changed policy and legal text and obtain the publisher's approval before committing and pushing the update:

   ```sh
   git add README.md scripts/build.py content/ index.html privacy/ legal/ support/ en/ es/
   git commit -m "Update published PoolPilot information pages"
   git push -u origin main
   ```

2. Check the Pages deployment and every language link. `.nojekyll` ensures the prebuilt HTML is served as-is.

The root URL is `https://arnaudmourcel47-spec.github.io/poolpilot-site/`. Its privacy, support and legal URLs follow the table above.

Official GitHub instructions: [Create a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository), [configure a Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site), [set a private commit email](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

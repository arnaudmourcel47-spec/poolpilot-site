# PoolPilot public site — publication pending

Static, dependency-free GitHub Pages source, separate from the iOS project. No app source, user records, photos, archives or IPA are included. **Nothing has been uploaded.** A local initial commit is prepared for the public repository; legal publication review remains open.

## Pages

| Language | Home | Privacy | Support | Legal notice |
| --- | --- | --- | --- | --- |
| Français | `/` | `/privacy/` | `/support/` | `/legal/` |
| English | `/en/` | `/en/privacy/` | `/en/support/` | `/en/legal/` |
| Español | `/es/` | `/es/privacy/` | `/es/support/` | `/es/legal/` |

The privacy pages started from the three drafts copied from the PoolPilot iOS project on 14 October 2026. This site copy now includes the publisher-confirmed EI and micro-entrepreneur status, SIREN and SIRET, postal address, telephone, contact email, planned effective date and support-email retention period. The original iOS files were not modified. The pages retain a publication-pending notice only for the applicable register, VAT status, hosting-provider telephone wording and App Privacy/build review.

## Required before public publication

1. Verify the applicable registration register and reference for the supplied SIREN/SIRET. Confirm the actual VAT regime and whether an intra-community VAT number applies; the publisher says he does not charge VAT, which alone does not establish the franchise en base. Confirm whether publishing PoolPilot matches the EI's declared activity.
2. Resolve the GitHub Pages host telephone requirement and confirm which GitHub entity is legally responsible for this Pages site through qualified legal review. The legal pages list GitHub, Inc. and GitHub B.V. as entities named in GitHub's documentation; they do not present GitHub B.V. as the confirmed contractual host. Do not invent a number. The GitHub Pages URLs are proposed, not live.
3. Review the exact distributed app build, Apple services, App Privacy answers, support-email retention implementation and public website's host-side practices. Do not infer that the absence of an analytics SDK proves no data collection by every platform integration.
4. Confirm that **16 October 2026** is the intended effective date even if first publication occurs later; record the actual publication date separately if needed.
5. After legal review, remove draft wording from the policies and legal notices and update `draft_badge`, `draft_text`, and the preparatory footer in `scripts/build.py` to approved public wording.
6. Rebuild the pages and run the checks below. Read all twelve pages once in a browser, including on a narrow screen.
7. Obtain explicit approval before creating/pushing the public repository or enabling Pages.

## Local build and preview

```sh
python3 scripts/build.py
python3 scripts/check_site.py
python3 -m http.server 8000
```

Open `http://localhost:8000/` while the server runs. The build uses only Python's standard library; the published pages need no JavaScript, fonts, CDN, analytics or cookies.

## Publish later, after approval

1. On GitHub, create a **public** repository named `poolpilot-site` under `arnaudmourcel47-spec`. Leave README, `.gitignore` and license options unselected, because this local repository already has content.
2. The local initial commit uses the publisher's already-public support email in its Git metadata. Before uploading, verify the commit tree and author identity. If the publisher prefers a GitHub `noreply` address, replace the local commit author email **before** pushing, using the exact address shown in GitHub Settings → Emails. Do not substitute a guessed address.

3. Confirm the legal content is final, then push the prepared commit only after explicit approval:

   ```sh
   git push -u origin main
   ```

4. In that repository, open **Settings → Pages → Build and deployment**. Choose **Deploy from a branch**, branch `main`, folder `/(root)`, then save. `.nojekyll` ensures the prebuilt HTML is served as-is.
5. Check the Pages deployment and every language link. Use the resulting public privacy URLs in App Store Connect after legal review.

The expected root URL is `https://arnaudmourcel47-spec.github.io/poolpilot-site/`. Its privacy, support and legal URLs follow the table above. No URL is live until the public repository is created, pushed, and Pages enabled.

Official GitHub instructions: [Create a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository), [configure a Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site), [set a private commit email](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

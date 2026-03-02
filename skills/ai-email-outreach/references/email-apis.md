# Email Outreach API Reference

## Email Finder APIs

### Apollo.io

**Base URL:** `https://api.apollo.io/v1`

**Authentication:** Header `x-api-key: YOUR_API_KEY`

**Free Tier:** Unlimited email credits (fair use), 4k requests/day

```python
# Search for people
POST /mixed_people/search
{
    "organization_domains": ["company.com"],
    "person_titles": ["VP Engineering", "CTO"],
    "person_seniorities": ["director", "vp", "c_suite"],
    "email_status": ["verified"],
    "per_page": 25
}

# Enrich a person
POST /people/match
{
    "first_name": "John",
    "last_name": "Doe",
    "organization_name": "Acme Corp"
}
```

### Snov.io

**Base URL:** `https://api.snov.io/v1`

**Authentication:** Bearer token

**Pricing:** $30/mo starter

```python
# Find email by domain
POST /get-emails-from-url
{
    "domain": "company.com",
    "type": "all"
}

# Find email by name
POST /get-emails-from-names
{
    "first_name": "John",
    "last_name": "Doe",
    "domain": "company.com"
}
```

### Findymail

**Base URL:** `https://app.findymail.com/api`

**Pricing:** $49/mo, only charges for valid emails

```python
# Find email
POST /search/email
{
    "name": "John Doe",
    "domain": "company.com"
}
# Returns email only if verified (>95% accuracy)
```

### Icypeas

**Base URL:** `https://api.icypeas.com`

**Pricing:** ~$7/1000 emails (cheapest)

```python
# Email finder
POST /email-finder
{
    "firstname": "John",
    "lastname": "Doe",
    "company": "company.com"
}
```

---

## Email Verification APIs

### NeverBounce

**Base URL:** `https://api.neverbounce.com/v4`

```python
# Single verification
POST /single/check
{
    "key": "API_KEY",
    "email": "test@company.com"
}

# Response results:
# "valid" - Safe to send
# "invalid" - Do not send
# "disposable" - Temporary email
# "catchall" - Accepts all (risky)
# "unknown" - Could not verify
```

### ZeroBounce

**Base URL:** `https://api.zerobounce.net/v2`

```python
# Validate email
GET /validate?api_key=KEY&email=test@company.com

# Response status:
# "valid", "invalid", "catch-all", "unknown",
# "spamtrap", "abuse", "do_not_mail"
```

### Verifalia

**Base URL:** `https://api.verifalia.com/v2.4`

**Authentication:** Basic Auth

```python
# Submit verification
POST /email-validations
{
    "entries": [{"inputData": "test@company.com"}]
}

# 30+ verification steps, 99% accuracy
```

---

## Prospect Research APIs

### Proxycurl (LinkedIn Data)

**Base URL:** `https://nubela.co/proxycurl/api`

```python
# Get LinkedIn profile
GET /v2/linkedin
?linkedin_profile_url=https://linkedin.com/in/johndoe

# Returns: headline, summary, experiences, education,
# skills, activities (recent posts)
```

### BuiltWith (Tech Stack)

**Base URL:** `https://api.builtwith.com`

```python
# Get tech stack
GET /v21/api.json
?KEY=API_KEY&LOOKUP=company.com

# Returns: CMS, analytics, frameworks, hosting, etc.
```

### Crunchbase (Company Data)

**Base URL:** `https://api.crunchbase.com/v4`

```python
# Company lookup
GET /entities/organizations/company-name

# Returns: funding rounds, employee count,
# recent news, investors
```

---

## Waterfall Enrichment Pattern

Check multiple providers sequentially for 80% hit rate:

```python
def find_verified_email(name, domain):
    # Try Apollo first (free tier)
    email = apollo_search(name, domain)
    if email and verify_email(email):
        return email

    # Try Snov.io
    email = snov_search(name, domain)
    if email and verify_email(email):
        return email

    # Try Findymail (highest accuracy)
    email = findymail_search(name, domain)
    if email:  # Already verified
        return email

    return None

def verify_email(email):
    result = neverbounce_check(email)
    return result == "valid"
```

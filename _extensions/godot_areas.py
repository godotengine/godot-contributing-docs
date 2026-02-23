"""
A directive for organization/areas.rst to render the area tables.
"""
import dataclasses

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.roles import XRefRole
import re

area_table_rows = ("Communication", "GitHub reviews", "GitHub labels", "Triage project", "Maintainers")

channel_re = re.compile(r'#([\w-]+)')
godot_team_re = re.compile(r'@godotengine/([\w-]+)')
labels_re = re.compile(r'<gh-label>(.+?)</gh-label>')
triage_re = re.compile(r'<gh-triage project=(\d+)>(.*?)</gh-triage>')
lead_re = re.compile(r'<lead>(.*?)</lead>')


def transform_channels(match: re.Match):
    old_value = match.group(1)
    transformed = f'<a href="https://chat.godotengine.org/channel/{old_value}">#{old_value}</a>'
    return transformed


def transform_github_teams(match: re.Match):
    old_value = match.group(1)
    transformed = f'<a href="https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2F{old_value}">@godotengine/{old_value}</a>'
    return transformed


def transform_github_labels(match: re.Match):
    old_value = match.group(1)
    transformed = f'<span style="white-space: nowrap;"><code class="docutils literal notranslate"><span class="pre">{old_value}</span></code> (<a href="https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3A{old_value}">issues</a>, <a href="https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3A{old_value}">PRs</a>)</span>'
    return transformed


def transform_github_triage(match: re.Match):
    number = match.group(1)
    name = match.group(2)
    transformed = f'<a href="https://github.com/orgs/godotengine/projects/{number}">{name}</a>'
    return transformed


def transform_lead(match: re.Match):
    name = match.group(1)
    transformed = f'<span class="team-lead">{name}</span>'
    return transformed


class TableDirective(Directive):
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {column.lower().replace(" ", "_"): str for column in area_table_rows}

    def run(self):
        # Create a table node with the parsed header and data
        table = nodes.container()
        table.setdefault('classes', []).append("gdarea-table")

        # Create and add the table body
        for column_title in area_table_rows:
            row_text = self.options.get(column_title.lower().replace(" ", "_"), '')
            if not row_text:
                continue

            row = nodes.container()

            entry = nodes.container()
            entry.setdefault('classes', []).append("gdarea-table-header")
            entry += nodes.paragraph(text=column_title)
            row += entry

            row_text = channel_re.sub(transform_channels, row_text)
            row_text = godot_team_re.sub(transform_github_teams, row_text)
            row_text = labels_re.sub(transform_github_labels, row_text)
            row_text = triage_re.sub(transform_github_triage, row_text)
            row_text = lead_re.sub(transform_lead, row_text)

            entry = nodes.container()
            paragraph = nodes.paragraph()
            paragraph += nodes.raw('', row_text, format='html')
            entry += paragraph
            row += entry

            table += row

        return [table]


class TeamRole(XRefRole):
    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        # Hacky, but apparently easiest way to get normal link behavior.
        role = self.target.lower().replace(" ", "_")

        if self.has_explicit_title:
            self.title = f"◆ {self.title}"
        else:
            self.title = f"◆ {self.title} team"

        self.target = f"team_{role}"
        self.has_explicit_title = True

        self.refdomain, self.reftype = "std", "ref"
        self.classes = ['xref', self.reftype]

        if self.disabled:
            return self.create_non_xref_node()
        else:
            return self.create_xref_node()


def setup(app):
    app.add_directive('gdareatable', TableDirective)
    app.add_role('team', TeamRole())

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
